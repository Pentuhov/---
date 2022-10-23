#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pair:

    def __init__(self, first, second):
        self.first = first
        self.second = second


    def display(self):
        print(self.first, self.second)

    def addition(self, term):
        if isinstance(term, Pair):
            return Pair(self.first + self.second, term.first + term.second)

    def multiply(self, term):
        if isinstance(term, Pair):
            return Pair(self.first * self.second, term.first * term.second)


class Complex(Pair):

    def addition(self, term):
        if isinstance(term, Complex):
            return Complex(self.first * term.first - self.second * term.second, self.first * term.second + self.second * term.first)

    def sub(self, term):
        if isinstance(term, Complex):
            return Pair(self.first - self.second, term.first - term.second)


if __name__ == '__main__':
    num1 = Pair(4, 6)
    num2 = Pair(10, 14)
    num1.multiply(num2).display()
    num1.addition(num2).display()
    complex1 = Complex(5, 13)
    complex2 = Complex(12, 3)
    complex1.sub(complex2).display()
    complex1.addition(complex2).display()