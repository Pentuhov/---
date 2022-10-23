#!/usr/bin/env python3
# -*- coding^ utf-8 -*-

from random import randint


class MyError(Exception):
    def __init__(self, text):
        self.txt = text

try:
    N = int(input('строки: '))
    M = int(input('столбцы: '))
    c = int(input('начало диапазона целых чисел: '))
    d = int(input('конец диапазона целых чисел: '))
    if (N <= 0 ) or (M <= 0):
        raise MyError('Число должно быть положительным!')
    if d < c:
        raise MyError('Начало диапазона не может быть больше конца!')
except MyError as s:
    print("Исключение:")
    print(s)
else:
    lst = [[randint(c, d) for _ in range(N)] for _ in range(M)]
    for i in lst:
        print()
        for j in i:
            print(j, end=" ")
    print()



