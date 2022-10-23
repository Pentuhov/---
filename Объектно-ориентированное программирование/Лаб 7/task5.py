#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Frame, StringVar, Label, Radiobutton, TOP, LEFT

persons = {
    'Вася': '+7 928 333-13-42',
    'Петя': '+7 928 113-12-67',
    'Маша': '+7 928 223-25-89'
}

def get_contact():
    label.config(text=persons[var.get()])


if __name__ == "__main__":
    root = Tk()
    root.title('Группа')
    root.resizable(height=False, width=False)
    f_left = Frame(root)
    f_left.pack(side=LEFT)
    label = Label(root, justify='center', width=40, text='Выберите студента', font=18)
    label.pack(side=LEFT, expand=True)
    var = StringVar()
    for name in persons.keys():
        Radiobutton(f_left, width=20, font=20, text=name, indicatoron=0, variable=var,
                    value=name, command=get_contact).pack(side=TOP)
    root.mainloop()