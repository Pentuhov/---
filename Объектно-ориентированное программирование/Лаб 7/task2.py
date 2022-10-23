#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Label, Button, Entry, END, Tk, CENTER

"""
Решите задачу: напишите программу, состоящую из семи кнопок, цвета которых
соответствуют цветам радуги. При нажатии на ту или иную кнопку в текстовое поле должен
вставляться код цвета, а в метку – название цвета.
атеричной кодировке: #ff0000 – красный, #ff7d00 – оранжевый,
#ffff00 – желтый, #00ff00 – зеленый, #007dff – голубой, #0000ff – синий, #7d00ff –
фиолетовый.

"""

class Frame(Tk):
    def __init__(self):
        super().__init__()
        self.title('Task2')
        self.geometry("189x222")
        self.lbl = Label(text="", width=230)
        self.e1 = Entry(width=230, justify=CENTER)
        dar = { '#ff0000': 'Красный',
        '#ff7d00': 'Оранжевый',
        '#ffff00': 'Желтый',
        '#00ff00': 'Зеленый',
        '#007dff': 'Голубой',
        '#0000ff': 'Синий',
        '#7d00ff': 'Фиолетовый' }

        for colour in dar.keys():
            sa = lambda c=colour, ruc=dar[colour]: self.onclick(c, ruc)
            b = Button(text='', command=sa, bg=colour, width=50, height=1)

            self.lbl.pack()
            self.e1.pack()
            b.pack()

    def onclick(self, colour, ru_colour):
        self.e1.delete(0, END)
        self.e1.insert(0, colour)
        self.lbl['text'] = ru_colour


if __name__ == '__main__':
    root = Frame()

    root.mainloop()