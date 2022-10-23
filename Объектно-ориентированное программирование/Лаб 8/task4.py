#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import Tk, Canvas, ARC

# Создать подобное изображение

if __name__ == '__main__':

    # Создаем графический интерфейс
    root = Tk()
    root.title('Рисунок')
    root.geometry('500x500')

    # Создаем окно Canvas
    c = Canvas(root, width=500, height=400, bg='white')
    c.pack()

    # Создаем основу дома и солнце
    circle = c.create_oval(383, 18, 450, 84, fill="#FFFF00")
    rectangle = c.create_rectangle(129, 143, 340, 360, fill='orange')
    triangle = c.create_polygon(232, 30, 90, 144, 375, 143, fill='#804040')
    # Создаем кота
    c.create_rectangle(119, 294, 48, 336, fill='#804040')
    c.create_rectangle(59, 374, 48, 336, fill='#804040')
    c.create_rectangle(119, 374, 108, 336, fill='#804040')
    triangle3 = c.create_polygon(81, 253, 76, 266, 83, 271, fill='#804040')
    triangle4 = c.create_polygon(64, 253, 57, 271, 65, 266, fill='#804040')
    line1 = c.create_line(81, 283, 100, 287)
    line2 = c.create_line(80, 288, 96, 296)
    line3 = c.create_line(58, 284, 40, 289)
    line4 = c.create_line(58, 289, 41, 295)
    circle2 = c.create_oval(26, 296, 55, 265, fill="#400000")
    circle3 = c.create_oval(53, 316, 38, 301, fill="#400000")
    circle4 = c.create_oval(41, 316, 26, 301, fill="#400000")
    circle5 = c.create_oval(29, 281, 31, 274, fill="white")
    circle6 = c.create_oval(36, 278, 34, 276, fill="black")
    circle7 = c.create_oval(40, 281, 32, 274, fill="white")
    circle8 = c.create_oval(57, 278, 25, 276, fill="black")

    # Добавляем детали к дому
    rectangle2 = c.create_rectangle(200, 160, 265, 227, fill='white')
    line5 = c.create_line(232, 160, 232, 227)
    line6 = c.create_line(200, 195, 265, 195)

    # Создаем цикл, для вывода травы
    x = 0
    while x < 500:
        c.create_arc(x, 1005, x+30, 350, start=150, extent=-99, style=ARC, width=3, outline='brown')
        x += 15

    # Запуск программы
    root.mainloop()