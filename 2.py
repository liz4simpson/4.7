#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk


def update_color(color_codes, color_names):
    color_code_label.config(text=f"Код цвета: {color_codes}")
    color_name_label.config(text=f"Название цвета: {color_names}")


def button_clicked(color_codes, color_names):
    update_color(color_codes, color_names)


root = tk.Tk()
root.title("Rainbow Colors")

colors = {
    "Красный": "#ff0000",
    "Оранжевый": "#ff7d00",
    "Желтый": "#ffff00",
    "Зеленый": "#00ff00",
    "Голубой": "#007dff",
    "Синий": "#0000ff",
    "Фиолетовый": "#7d00ff"
}

color_code_label = tk.Label(root, text="Код цвета: ")
color_code_label.pack()

color_name_label = tk.Label(root, text="Название цвета: ")
color_name_label.pack()

for color_name, color_code in colors.items():
    button = tk.Button(root, text=color_name, bg=color_code, width=10,
                       command=lambda c=color_code, n=color_name: button_clicked(c, n))
    button.pack(pady=5)

root.mainloop()