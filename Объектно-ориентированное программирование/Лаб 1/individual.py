#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

"""
Поле first — целое число, целая часть числа; поле second — положительное целое число,
дробная часть числа. Реализовать метод multiply() — умножение на произвольное целое
число типа int. Метод должен правильно работать при любых допустимых значениях first и
second.
"""

class Rational:

    def __init__(self, first, second):
        self.first = first
        self.second = second
        if (self.first <= 0) or (self.second <= 0):
            raise ValueError()

    def read(self):
        self.first = int(input("Введите целую часть числа "))
        self.second = int(input("Введите дробную часть числа "))

    def display(self):
        print(f"Число с плавающей точкой {self.first}.{self.second}")

#посчитать через логарифм кол-во цифр в числе
    def multiply(self, other):
        length = int(math.log10(self.second)) + 1
        second = (self.second * other) % (10 ** length)
        fractal = (self.second * other) // (10 ** length)
        first = self.first * other + fractal
        return Rational(first, second)


def make_rational(first, second):
    if second <= 0:
        raise ValueError()
    else:
        return Rational(first, second)


if __name__ == '__main__':
    newNum = Rational(12, 55)
    newNum.display()
    newNum.multiply(5)
    make_num = make_rational(45, 34)
    make_num.display()
    number = make_num.multiply(16)
    number.display()
