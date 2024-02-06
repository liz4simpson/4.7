#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk


def show_selected():
    selected_value.set(f"+ {selected_option.get()}")


root = tk.Tk()
root.title("Пример с Radiobutton")

selected_option = tk.StringVar()

selected_value = tk.StringVar()

radiobutton1 = tk.Radiobutton(root, text="Коля", width=8, height=3, variable=selected_option, value=7588615151,
                              indicatoron=False, command=show_selected, relief="flat")
radiobutton2 = tk.Radiobutton(root, text="Ваня", width=8, height=3, variable=selected_option, value=7512458621,
                              indicatoron=False, command=show_selected, relief="flat")
radiobutton3 = tk.Radiobutton(root, text="Вася", width=8, height=3, variable=selected_option, value=7321458464,
                              indicatoron=False, command=show_selected, relief="flat")

label = tk.Label(root, textvariable=selected_value, width=20, height=5)

radiobutton1.grid(row=0, column=0, sticky="w", padx=10, pady=2)
radiobutton2.grid(row=1, column=0, sticky="w", padx=10, pady=2)
radiobutton3.grid(row=2, column=0, sticky="w", padx=10, pady=2)
label.grid(row=0, column=1, rowspan=3, padx=10, pady=10)

root.mainloop()