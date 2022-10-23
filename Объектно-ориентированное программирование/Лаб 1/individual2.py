#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать класс Money для работы с денежными суммами. Число должно быть представлено
двумя полями: типа int для рублей и копеек. Дробная часть (копейки) при выводе на экран
должна быть отделена от целой части запятой. Реализовать сложение, вычитание, деление
сумм, деление суммы на дробное число, умножение на дробное число и операции
сравнения.
"""

class Money:

    def __init__(self, rub=0, kop=0):
        self.rub = int(rub)
        self.kop = int(kop)
        if (self.rub < 0) or (self.kop < 0):
            raise ValueError()

    def read(self):
        self.rub = input("Введите количество рублей ")
        self.kop = input("Введите количество копеек ")

    def display(self):
        print(f"Сумма -  {self.rub},{self.kop} рублей")

    def add(self, rhs):
        if isinstance(rhs, Money):
            a1 = float(str(self.rub) + "." + str(self.kop))
            a2 = float(str(rhs.rub) + "." + str(rhs.kop))
            return print(a1 + a2, "рублей в сумме")
        else:
            raise ValueError()
        # Вычитание

    def sub(self, rhs):
        if isinstance(rhs, Money):
            a1 = float(str(self.rub) + "." + str(self.kop))
            a2 = float(str(rhs.rub) + "." + str(rhs.kop))
            return print(round(abs(a1 - a2), 2), " - разница между 2 суммами")
        else:
            raise ValueError()

        # Умножение на дробь.
    def mul(self):
        frc = input("Введите дробь в виде Число/Число ")
        parts = list(map(int, frc.split('/', maxsplit=1)))
        a1 = float(str(self.rub) + "." + str(self.kop))
        a2 = (a1 * int(parts[0]))/int(parts[1])
        return print("Результат умножения на дробь", round(a2, 2))

        # Деление
    def div(self, rhs):
        if isinstance(rhs, Money):
            a1 = float(str(self.rub) + "." + str(self.kop))
            a2 = float(str(rhs.rub) + "." + str(rhs.kop))
            return print("Результат деления - ", round(a1 / a2, 2))
        else:
            raise ValueError()

        # Сравнение
    def compare(self, rhs):
        if isinstance(rhs, Money):
            a2 = float(str(self.rub) + "." + str(self.kop))
            a1 = float(str(rhs.rub) + "." + str(rhs.kop))
            if a1 > a2:
                print("Первая сумма больше")
            elif a1 < a2:
                print("Вторая сумма больше")
            else:
                print("Суммы равны")


if __name__ == '__main__':
    r1 = Money(35, 50)
    r1.display()
    r2 = Money()
    r2.read()
    r2.display()
    r3 = r2.add(r1)
    r4 = r2.sub(r1)
    r5 = r2.div(r1)
    r6 = r2.mul()
    r7 = r2.compare(r1)
