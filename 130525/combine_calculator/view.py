import tkinter as tk
from tkinter import ttk

class CombinatorialView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Калькулятор комбинаторики")
        self._setup_ui()

    def _setup_ui(self):
        main_frame = ttk.Frame(self)
        main_frame.pack(padx=10, pady=10)

        # Выбор типа операции
        ttk.Label(main_frame, text="Тип операции:").grid(row=0, column=0, sticky=tk.W)
        self.operation_var = tk.StringVar()
        self.operation_combobox = ttk.Combobox(
            main_frame,
            textvariable=self.operation_var,
            values=[
                "Перестановки без повторений",
                "Перестановки с повторениями",
                "Сочетания без повторений",
                "Сочетания с повторениями",
                "Размещения без повторений",
                "Размещения с повторениями"
            ],
            state="readonly"
        )
        self.operation_combobox.grid(row=0, column=1, pady=5)
        self.operation_combobox.current(0)

        # Поля ввода
        self.n_label = ttk.Label(main_frame, text="n:")
        self.n_label.grid(row=1, column=0, sticky=tk.W)
        self.n_entry = ttk.Entry(main_frame)
        self.n_entry.grid(row=1, column=1, pady=5)

        self.k_label = ttk.Label(main_frame, text="k:")
        self.k_label.grid(row=2, column=0, sticky=tk.W)
        self.k_entry = ttk.Entry(main_frame)
        self.k_entry.grid(row=2, column=1, pady=5)
        self.k_label.grid_remove()
        self.k_entry.grid_remove()

        self.repeats_label = ttk.Label(main_frame, text="Повторения (через запятую):")
        self.repeats_entry = ttk.Entry(main_frame)
        self.repeats_label.grid_remove()
        self.repeats_entry.grid_remove()

        # Кнопка расчета
        self.calculate_button = ttk.Button(main_frame, text="Рассчитать")
        self.calculate_button.grid(row=4, columnspan=2, pady=10)

        # Результат
        self.result_label = ttk.Label(main_frame, text="Результат:")
        self.result_label.grid(row=5, column=0, sticky=tk.W)
        self.result_var = tk.StringVar()
        self.result_display = ttk.Label(main_frame, textvariable=self.result_var)
        self.result_display.grid(row=5, column=1, sticky=tk.W)

        # Обработчик изменения операции
        self.operation_combobox.bind("<<ComboboxSelected>>", self._update_input_fields)

    def _update_input_fields(self, event=None):
        operation = self.operation_var.get()
        if "Перестановки с повторениями" in operation:
            self.k_label.grid_remove()
            self.k_entry.grid_remove()
            self.repeats_label.grid()
            self.repeats_entry.grid()
        elif "Сочетания с повторениями" in operation or "Размещения" in operation:
            self.k_label.grid()
            self.k_entry.grid()
            self.repeats_label.grid_remove()
            self.repeats_entry.grid_remove()
        else:
            self.k_label.grid_remove()
            self.k_entry.grid_remove()
            self.repeats_label.grid_remove()
            self.repeats_entry.grid_remove()

    def get_inputs(self):
        operation = self.operation_var.get()
        inputs = {}
        try:
            inputs['n'] = int(self.n_entry.get())

            if "Сочетания" in operation or "Размещения" in operation:
                inputs['k'] = int(self.k_entry.get())

            if "Перестановки с повторениями" in operation:
                repeats = list(map(int, self.repeats_entry.get().split(',')))
                inputs['repeats'] = repeats

            return inputs
        except ValueError:
            raise ValueError("Некорректный ввод данных")

    def show_result(self, result):
        self.result_var.set(str(result))

    def show_error(self, message):
        self.result_var.set("Ошибка: " + message)