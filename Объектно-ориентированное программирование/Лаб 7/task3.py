#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, END, Label, Button, Entry, CENTER

"""
Решите задачу: перепишите программу из пункта 8 так, чтобы интерфейс выглядел
примерно следующим образом: -----
"""

class Frame(Tk):
    def __init__(self):
        super().__init__()
        self.title('Task2')
        self.geometry("270x102")
        self.lbl = Label(text="", width=200)
        self.e1 = Entry(width=30, justify=CENTER)
        dar = { '#ff0000': 'Красный',
        '#ff7d00': 'Оранжевый',
        '#ffff00': 'Желтый',
        '#00ff00': 'Зеленый',
        '#007dff': 'Голубой',
        '#0000ff': 'Синий',
        '#7d00ff': 'Фиолетовый' }
        for colour in dar.keys():

            sa = lambda c=colour, ruc=dar[colour]: self.onclick(c, ruc)
            b = Button(text='', command=sa, bg=colour, width=1, height=1, justify=CENTER)
            self.lbl.pack()
            self.e1.pack()
            b.pack(side='left', fill='x', ipadx=10, padx=1)


    def onclick(self, colour, ru_colour):
        self.e1.delete(0, END)
        self.e1.insert(0, colour)
        self.lbl['text'] = ru_colour


if __name__ == '__main__':
    root = Frame()
    root.mainloop()