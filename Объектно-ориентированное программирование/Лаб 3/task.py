#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный
номер объекта, и свойство, в котором хранится принадлежность команде. У солдат есть
метод "иду за героем", который в качестве аргумента принимает объект типа "герой". У
героев есть метод увеличения собственного уровня.
В основной ветке программы создается по одному герою для каждой команды. В цикле
генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
Солдаты разных команд добавляются в разные списки.
Измеряется длина списков солдат противоборствующих команд и выводится на экран. У
героя, принадлежащего команде с более длинным списком, увеличивается уровень.
Отправьте одного из солдат первого героя следовать за ним. Выведите на экран
идентификационные номера этих двух юнитов.
"""

from random import randint


class Hero:

    def __init__(self, team):
        self.team = team
        self.id = randint(1, 100000)
        self.lvl = 1

    def lvlup(self):
        self.lvl += 1


class Soldier(Hero):
    def follow_hero(self, unit):
        if isinstance(unit, Hero):
            return f'Солдат  команды {self.team} c номером {self.id}  идет за героем {unit.id}'


def create_teams():
    radiant_hero = Hero(1)
    dire_hero = Hero(2)
    radiant_squad = []
    dire_squad = []
    for i in range(100):
        unit = Soldier(randint(1, 2))
        if(unit.team == 1):
            radiant_squad.append(unit)
        else:
            dire_squad.append(unit)
    if (len(radiant_squad) > len(dire_squad)):
        radiant_hero.lvlup()
    else:
        dire_hero.lvlup()
    print(radiant_squad[1].follow_hero(radiant_hero))
    print(f'Id солдата -  {radiant_squad[1].id}\nId героя - {radiant_hero.id} Уровень героя {radiant_hero.lvl}')

if __name__ == '__main__':
    create_teams()

