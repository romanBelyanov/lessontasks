import tkinter as tk
from tkinter import ttk, colorchooser, messagebox
import math


class ShapeDrawerApp:
    def __init__(self, master):
        self.master = master
        master.title("Генератор фигур")

        # Настройка Canvas
        self.canvas = tk.Canvas(master, width=400, height=400, bg='white')
        self.canvas.pack(pady=20)

        # Выбор фигуры
        self.shape_label = ttk.Label(master, text="Выберите фигуру:")
        self.shape_label.pack()

        self.shape_var = tk.StringVar()
        self.shape_combobox = ttk.Combobox(master, textvariable=self.shape_var,
                                           values=["Круг", "Квадрат", "Треугольник"])
        self.shape_combobox.current(0)
        self.shape_combobox.pack()

        # Выбор цвета
        self.color_button = ttk.Button(master, text="Выбрать цвет", command=self.choose_color)
        self.color_button.pack(pady=5)
        self.selected_color = "#000000"  # Цвет по умолчанию

        # Ввод размера
        self.size_label = ttk.Label(master, text="Размер стороны/радиуса:")
        self.size_label.pack()

        self.size_entry = ttk.Entry(master)
        self.size_entry.pack()

        # Кнопка рисования
        self.draw_button = ttk.Button(master, text="Нарисовать", command=self.draw_shape)
        self.draw_button.pack(pady=10)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.selected_color = color

    def draw_shape(self):
        # Очистка холста
        self.canvas.delete("all")

        # Получение параметров
        shape_type = self.shape_var.get()
        size = self.size_entry.get()

        # Валидация ввода
        try:
            size = float(size)
            if size <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Ошибка", "Введите положительное число для размера")
            return

        # Координаты центра
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        center_x = canvas_width // 2
        center_y = canvas_height // 2

        # Рисование фигуры
        if shape_type == "Круг":
            radius = size
            self.canvas.create_oval(
                center_x - radius,
                center_y - radius,
                center_x + radius,
                center_y + radius,
                fill=self.selected_color,
                outline=self.selected_color
            )
        elif shape_type == "Квадрат":
            half_size = size / 2
            self.canvas.create_rectangle(
                center_x - half_size,
                center_y - half_size,
                center_x + half_size,
                center_y + half_size,
                fill=self.selected_color,
                outline=self.selected_color
            )
        elif shape_type == "Треугольник":
            height = (math.sqrt(3) / 2) * size
            points = [
                center_x, center_y - height / 2,  # Верхняя точка
                          center_x - size / 2, center_y + height / 2,  # Левая нижняя
                          center_x + size / 2, center_y + height / 2  # Правая нижняя
            ]
            self.canvas.create_polygon(
                points,
                fill=self.selected_color,
                outline=self.selected_color
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeDrawerApp(root)
    root.mainloop()