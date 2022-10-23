#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, END, Text, Entry, Button, DISABLED, NORMAL,RAISED, ACTIVE
from tkinter import filedialog as fd

def opening(event):
    text.delete(1.0, END)
    name = fd.askopenfilename()
    with open(name, 'r', encoding="utf-8") as f:
        data = f.read()
    text.insert(1.0, data)


def save(event):
    save_file = fd.asksaveasfilename(defaultextension=".txt", filetypes=(("Текстовый файл", "*.txt"),))
    data = text.get(1.0, END)
    with open(save_file, 'w', encoding="utf-8") as f:
        f.write(data)


if __name__ == '__main__':
    root = Tk()
    text = Text(width=87, height=80)
    ent = Entry(width=20)
    but1 = Button(text='Открыть', width=8, pady=5)
    but2 = Button(text='Сохранить', width=8, pady=5)
    but1.bind('<ButtonRelease-1>', opening)
    but2.bind('<ButtonRelease-1>', save)
    ent.pack()
    but1.pack()
    but2.pack()
    text.pack()
    root.mainloop()
