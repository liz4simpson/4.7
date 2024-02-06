#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk


class Calculator:
    def __init__(self, roote):
        self.root = roote
        self.root.title("Простой калькулятор")

        self.num1_entry = tk.Entry(roote, width=10)
        self.num1_entry.grid(row=0, column=0, padx=5, pady=5)

        self.operator_label = tk.Label(roote, text="", width=2)
        self.operator_label.grid(row=0, column=1, padx=5, pady=5)

        self.num2_entry = tk.Entry(roote, width=10)
        self.num2_entry.grid(row=0, column=2, padx=5, pady=5)

        self.result_label = tk.Label(roote, text="Результат: ", width=20)
        self.result_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.operations = {
            "сложение": "+",
            "вычитание": "-",
            "умножение": "*",
            "деление": "/"
        }

        self.add_button = tk.Button(roote, text="Сложение", command=lambda: self.calculate("сложение"))
        self.add_button.grid(row=2, column=0, padx=5, pady=5)

        self.subtract_button = tk.Button(roote, text="Вычитание", command=lambda: self.calculate("вычитание"))
        self.subtract_button.grid(row=2, column=1, padx=5, pady=5)

        self.multiply_button = tk.Button(roote, text="Умножение", command=lambda: self.calculate("умножение"))
        self.multiply_button.grid(row=2, column=2, padx=5, pady=5)

        self.divide_button = tk.Button(roote, text="Деление", command=lambda: self.calculate("деление"))
        self.divide_button.grid(row=3, column=0, padx=5, pady=5)

    def calculate(self, operation):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())

            if operation in self.operations:
                operator = self.operations[operation]
                result = eval(f"{num1} {operator} {num2}")

                self.operator_label.config(text=operation)
                self.result_label.config(text=f"Результат: {result}")
            else:
                self.result_label.config(text="Ошибка: Неподдерживаемая операция")

        except ValueError:
            self.result_label.config(text="Ошибка: введите число")


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
    