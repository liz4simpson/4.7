#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
import os


class FileEditorApp:
    def __init__(self, roote):
        self.root = roote
        self.root.title("Текстовый редактор")

        self.entry_filename = tk.Entry(roote, width=30)
        self.entry_filename.grid(row=0, column=0, padx=5, pady=5)

        open_button = tk.Button(roote, text="Открыть", command=self.open_file)
        open_button.grid(row=0, column=1, padx=5, pady=5)

        save_button = tk.Button(roote, text="Сохранить", command=self.save_file)
        save_button.grid(row=0, column=2, padx=5, pady=5)

        self.text_editor = tk.Text(roote, height=10, width=50)
        self.text_editor.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    def open_file(self):
        filename = self.entry_filename.get()
        try:
            with open(os.path.join(os.path.dirname(__file__), filename), 'r') as file:
                content = file.read()
                self.text_editor.delete(1.0, tk.END)
                self.text_editor.insert(tk.END, content)
        except FileNotFoundError:
            print("Ошибка: Файл не найден")

    def save_file(self):
        filename = self.entry_filename.get()
        filepath = os.path.join(os.path.dirname(__file__), filename)
        content = self.text_editor.get(1.0, tk.END)
        with open(filepath, 'w') as file:
            file.write(content)
        print("Информация: Файл успешно сохранен")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileEditorApp(root)
    root.mainloop()