#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dataclasses import dataclass, field
import sys
from typing import List
import xml.etree.ElementTree as ET


class IllegalNumberError(Exception):
    def __init__(self, number, message="Illegal number"):
        self.number = number
        self.message = message
        super(IllegalNumberError, self).__init__(message)

    def __str__(self):
        return f"{self.number} -> {self.message}"


# Класс пользовательского исключения в случае, если неверно
# введенны данные.
class IllegalTimeError(Exception):
    pass


# Класс пользовательского исключения в случае, если введенная
# команда является недопустимой.
class UnknownCommandError(Exception):
    def __init__(self, command, message="Unknown command"):
        self.command = command
        self.message = message
        super(UnknownCommandError, self).__init__(message)

    def __str__(self):
        return f"{self.command} -> {self.message}"
@dataclass(frozen=True)
class Shops:
    name: str
    product: str
    price: int


@dataclass
class Store:
    shops: List[Shops] = field(default_factory=lambda: [])

    def add(self, name: str, product: str, price: int) -> None:
        self.shops.append(
            Shops(
                name=name,
                product=product,
                price=price
            )
        )
        self.shops.sort(key=lambda Shops: Shops.name)

    def __str__(self):
        # Заголовок таблицы.
        table = []
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        table.append(line)
        table.append(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "No",
                "Магазин.",
                "Товар",
                "Цена"
            )
        )
        table.append(line)
        for idx, Shops in enumerate(self.shops, 1):
            table.append(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    Shops.name,
                    Shops.product,
                    Shops.price
                )
            )
        table.append(line)
        return '\n'.join(table)

    def select(self, name: str) -> None:
        cout: int = 0
        for i, shop in enumerate(self.shops, 1):
            if (shop.name == name):
                cout +=1
                print(
                    ' |{} -  {:<5} |{} -  {:<5} |'.format('product',
                        shop.product,'price',
                        shop.price
                    )
                )
        if(cout == 0):
            print("Такого магазина нет")

    def load(self, filename: str) -> None:
        with open(filename, 'r', encoding='utf8') as fin:
            xml: str = fin.read()
            parser = ET.XMLParser(encoding="utf8")
            tree = ET.fromstring(xml, parser=parser)
            self.shops = []
            for shop_element in tree:
                name, product, price = None, None, None
                for element in shop_element:
                    if element.tag == 'name':
                        name = element.text
                    elif element.tag == 'product':
                        product = element.text
                    elif element.tag == 'price':
                        price = int(element.text)
                    if name is not None and product is not None \
                            and price is not None:
                        self.shops.append(
                            Shops(
                                name=name,
                                product=product,
                                price=price
                            )
                        )

    def save(self, filename) -> None:
        root = ET.Element('shops')
        for Shops in self.shops:
            shops_element = ET.Element('Shops')
            name_element = ET.SubElement(shops_element, 'name')
            name_element.text = Shops.name
            post_element = ET.SubElement(shops_element, 'product')
            post_element.text = Shops.product
            year_element = ET.SubElement(shops_element, 'price')
            year_element.text = str(Shops.price)
            root.append(shops_element)
        tree = ET.ElementTree(root)
        with open(filename, 'wb') as fout:
            tree.write(fout, encoding='utf8', xml_declaration=True)


if __name__ == '__main__':
    Store = Store()
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break
        elif command == 'add':
            # Запросить данные
            name = input("Название магазина? ")
            product = input("Товар? ")
            price = int(input("Цена? "))
            Store.add(name, product, price)
        elif command == 'list':
            # Вывести список.
            print(Store)
        elif command.startswith('select '):
            parts = command.split(maxsplit=1)
            print(parts[1])
            selected = Store.select(parts[1])
        elif command.startswith('load '):
            parts = command.split(maxsplit=1)
            Store.load(parts[1])
        elif command.startswith('save '):
            # Разбить команду на части для имени файла.
            parts = command.split(maxsplit=1)
            # Сохранить данные в файл.
            Store.save(parts[1])
        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить магазин;")
            print("list - вывести список магазинов;")
            print("select <магазин> - вывести товары из магазина;")
            print("load <имя_файла> - загрузить данные из файла;")
            print("save <имя_файла> - сохранить данные в файл;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)