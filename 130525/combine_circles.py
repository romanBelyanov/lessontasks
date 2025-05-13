import tkinter as tk
from tkinter import ttk
from itertools import permutations, combinations


class CombinatoricsVisualizer:
    def __init__(self, master):
        self.master = master
        master.title("Визуализатор комбинаторики")

        # Основные цвета
        self.colors = ['red', 'green', 'blue', 'yellow']

        # Настройка Canvas с прокруткой
        self.canvas = tk.Canvas(master, bg='white', width=600, height=400)
        self.scrollbar = ttk.Scrollbar(master, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Кнопки выбора
        self.btn_frame = ttk.Frame(master)
        self.btn_frame.pack(pady=10)

        ttk.Button(self.btn_frame, text="Перестановки из 3",
                   command=lambda: self.show_combinations('permutations')).pack(side="left", padx=5)
        ttk.Button(self.btn_frame, text="Сочетания из 4 по 2",
                   command=lambda: self.show_combinations('combinations')).pack(side="left", padx=5)
        ttk.Button(self.btn_frame, text="Размещения из 4 по 3",
                   command=lambda: self.show_combinations('arrangements')).pack(side="left", padx=5)

    def clear_canvas(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

    def show_combinations(self, comb_type):
        self.clear_canvas()

        if comb_type == 'permutations':
            elements = self.colors[:3]
            combs = list(permutations(elements))
            title = "Перестановки из 3 цветов"

        elif comb_type == 'combinations':
            elements = self.colors[:4]
            combs = list(combinations(elements, 2))
            title = "Сочетания из 4 по 2"

        elif comb_type == 'arrangements':
            elements = self.colors[:4]
            combs = list(permutations(elements, 3))
            title = "Размещения из 4 по 3"

        # Заголовок
        ttk.Label(self.scrollable_frame, text=title, font=('Arial', 12)).pack(pady=10)

        # Отображение комбинаций
        frame = ttk.Frame(self.scrollable_frame)
        frame.pack()

        row = col = 0
        for i, combo in enumerate(combs):
            if col == 5:  # 5 элементов в ряд
                row += 1
                col = 0

            combo_frame = ttk.Frame(frame)
            combo_frame.grid(row=row, column=col, padx=10, pady=5)

            # Отображение кругов
            for j, color in enumerate(combo):
                canvas = tk.Canvas(combo_frame, width=40, height=40, bg='white', highlightthickness=0)
                canvas.create_oval(5, 5, 35, 35, fill=color)
                canvas.pack(side="left", padx=2)

            col += 1

        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


if __name__ == "__main__":
    root = tk.Tk()
    app = CombinatoricsVisualizer(root)
    root.mainloop()