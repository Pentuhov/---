#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

class Real:

    def __init__(self, first, second):
        self.first = first
        self.second = second
        if (self.first < 0) or (self.second < 0):
            raise ValueError()

    def read(self):
        self.first = int(input("Введите целую часть числа "))
        self.second = int(input("Введите дробную часть числа "))

    def __str__(self):
        return f"{self.first}.{self.second}"

    def __repr__(self):
        return self.__str__()

    def display(self):
        print(f"Число с плавающей точкой {self.first}.{self.second}")

    def __mul__(self, other):  # *
        length = int(math.log10(self.second)) + 1
        second = (self.second * other) % (10 ** length)
        fractal = (self.second * other) // (10 ** length)
        first = self.first * other + fractal
        return Real(first, second)


if __name__ == '__main__':
    t1 = Real(12, 5)
    t2 = Real(6, 5)
    t1.display()
    print(t1 * 5)
