#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Label, Entry, Button, Tk
from math import sqrt

root = Tk()
root.title("tK")
w = root.winfo_screenwidth()  # ширина экрана
h = root.winfo_screenheight()  # высота экрана
w = w // 2 - 100  # середина экрана - половина ширины окна
h = h // 2 - 165  # середина экрана - половина высоты окна
root.geometry('100x165+{}+{}'.format(w, h))


def Plus():
    L.configure(text="{}".format(int(e1.get()) + int(e2.get())))


def Minus():
    L.configure(text="{}".format(int(e1.get()) - int(e2.get())))


def Umn():
    L.configure(text="{}".format(int(e1.get()) * int(e2.get())))


def Delenie():
    if int(e2.get()) == 0:
        L.configure(text="Делить на нуль нельзя!")
    else:
        L.configure(text="{}".format(int(e1.get()) / int(e2.get())))


def stepen():
    L.configure(text="{}".format(e1.get(), e2.get(), int(e1.get()) ** int(e2.get())))


def koren():
    if int(e1.get()) < 0:
        L.configure(text="Ошибка! Корень из отрицательного числа!")
    else:
        L.configure(text="Корень из {} = {}".format(e1.get(), sqrt(int(e1.get()))))


def cl():
    L.configure(text="0")
    e1.delete(0)
    e2.delete(0)
    e1.insert(0, 0)
    e2.insert(0, 0)


L = Label(text="0", bg="#ffffff", width=12)
L.grid(row=6, column=0)
e1 = Entry(text="", width=15)
e1.grid(row=0, column=0)
e2 = Entry(text="", width=15)
e2.grid(row=1, column=0)
b1 = Button(text="+", width=17, command=Plus)
b1.grid(row=2, column=0)
b2 = Button(text="-", width=17, command=Minus)
b2.grid(row=3, column=0)
b3 = Button(text="*", width=17, command=Umn)
b3.grid(row=4, column=0)
b4 = Button(text="/", width=17, command=Delenie)
b4.grid(row=5, column=0)
root.mainloop()