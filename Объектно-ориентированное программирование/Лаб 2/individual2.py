#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Нагрузка преподавателя за учебный год представляет собой список дисциплин,
преподаваемых им в течение года. Одна дисциплина представляется информационным
словарем с ключами: название дисциплины, семестр проведения, количество студентов,
количество часов аудиторных лекций, количество аудиторных часов практики, вид контроля
(зачет или экзамен). Реализовать класс WorkTeacher, моделирующий бланк назначенной
преподавателю нагрузки. Класс содержит фамилию преподавателя, дату утверждения,
список преподаваемых дисциплин, объем полной нагрузки в часах и в ставках. Дисциплины
в списке не должны повторяться. Объем в ставках вычисляется как частное от деления
объема в часах на среднюю годовую ставку, одинаковую для всех преподавателей кафедры.
Элемент списка преподаваемых дисциплин содержит дисциплину, количество часов,
выделяемых на зачет (0,35 ч на одного студента) или экзамен (0,5 ч на студента), сумму
часов по дисциплине. Реализовать добавление и удаление дисциплин; вычисление
суммарной нагрузки в часах и ставках. Должен осуществляться контроль за превышением
нагрузки более полутора ставок.

"""

class WorkTeacher:

    def __init__(self, sname, date, discipline):
        sgs = 100
        self.sname = sname
        self.date = date
        self.discipline = self.uniq(discipline)
        self.load = self.all_hours()
        self.stavka = self.load / sgs
        if (self.stavka > 1.5):
            print("Нагрузка превышена")

    # проверка на уникальность
    def uniq(self, discipline):
        unique = []
        for number in discipline:
            if number not in unique:
                unique.append(number)
        return unique

    def all_hours(self):
        all_hours = 0
        for i in self.discipline:
            all = i['hours_pract'] + i['hours_lekt']
            i['summ_hours'] = all
            all_hours += all
            if i['cont'] == 'exam':
                i['hours_for_student'] = 0.5
            else:
                i['hours_for_student'] = 0.35
        return all_hours

    def __getitem__(self, key):
        return self.discipline[key]

    def __setitem__(self, key, value):
        self.discipline[key] = value
        return self.discipline

    def size(self):
        return len(self.discipline)

    def display(self):
        print(f"Список предметов {self.discipline}")

    def add(self, other):
        self.discipline.append(other)
        self.all_hours()
        return self.discipline

    def remove(self, other):
        self.discipline.remove(other)
        return self.discipline

if __name__ == '__main__':
    math = {'name': "Algebra", 'term': 2, 'students': 45,
            'hours_lekt': 20, 'hours_pract': 40, 'cont': 'exam'}
    rus = {'name': "Ruskiy", 'term': 1, 'students': 80,
            'hours_lekt': 10, 'hours_pract': 30, 'cont': 'zachet'}
    litra = {'name': "Literatura", 'term': 3, 'students': 50,
           'hours_lekt': 20, 'hours_pract': 25, 'cont': 'zachet'}
    fizra = {'name': "Fizcultura", 'term': 1, 'students': 60,
             'hours_lekt': 10, 'hours_pract': 35, 'cont': 'zachet'}
    list_sub = [math, rus, litra]
    a = WorkTeacher('Иванов', '25.4.21', list_sub)
    a.add(fizra)
    a.display()
    print(a.size())
    a.remove(litra)
    a.display()
