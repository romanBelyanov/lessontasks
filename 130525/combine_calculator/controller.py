from model import CombinatorialModel
from view import CombinatorialView

class CombinatorialController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.calculate_button.configure(command=self.calculate)

    def calculate(self):
        try:
            operation = self.view.operation_var.get()
            inputs = self.view.get_inputs()
            result = None

            if operation == "Перестановки без повторений":
                result = self.model.calculate_permutations_without_repetitions(inputs['n'])
            elif operation == "Перестановки с повторениями":
                result = self.model.calculate_permutations_with_repetitions(
                    inputs['n'], inputs['repeats']
                )
            elif operation == "Сочетания без повторений":
                result = self.model.calculate_combinations_without_repetitions(
                    inputs['n'], inputs['k']
                )
            elif operation == "Сочетания с повторениями":
                result = self.model.calculate_combinations_with_repetitions(
                    inputs['n'], inputs['k']
                )
            elif operation == "Размещения без повторений":
                result = self.model.calculate_arrangements_without_repetitions(
                    inputs['n'], inputs['k']
                )
            elif operation == "Размещения с повторениями":
                result = self.model.calculate_arrangements_with_repetitions(
                    inputs['n'], inputs['k']
                )

            self.view.show_result(result)
        except Exception as e:
            self.view.show_error(str(e))

if __name__ == "__main__":
    model = CombinatorialModel()
    view = CombinatorialView()
    controller = CombinatorialController(model, view)
    view.mainloop()