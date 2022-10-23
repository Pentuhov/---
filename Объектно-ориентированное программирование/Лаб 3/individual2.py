#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
import math

class Array(ABC):

    def __init__(self, arr):
        self.arr = arr

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def each(self):
        pass

    @abstractmethod
    def display(self):
        pass

class AndArray(Array):

    def add(self, other):
        if isinstance(other, AndArray):
            adds = set(self.arr) & set(other.arr)
            return AndArray(adds)

    def each(self):
        for i, value in enumerate(self.arr):
            self.arr[i] = math.sqrt(value)
        return AndArray(self.arr)

    def display(self):
        for num in self.arr:
            print(num)

class OrArray(Array):

    def add(self, other):
        if isinstance(other, OrArray):
            adds = set(self.arr) | set(other.arr)
            return OrArray(adds)

    def each(self):
        for i, value in enumerate(self.arr):
            self.arr[i] = math.log(value)
        return OrArray(self.arr)

    def display(self):
        for num in self.arr:
            print(num)

if __name__ == '__main__':
    arr = AndArray([1, 4, 5, 7, 48, 55])
    arr2 = AndArray([4, 2, 5, 7, 34, 48])
    arr.add(arr2).display()
    arr.each().display()
    arr3 = OrArray([1, 4, 5, 7, 48, 55])
    arr4 = OrArray([4, 2, 5, 7, 34, 48])
    arr3.add(arr4).display()
    arr3.each().display()