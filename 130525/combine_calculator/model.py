from math import factorial

class CombinatorialModel:
    @staticmethod
    def calculate_permutations_without_repetitions(n):
        if n < 0:
            raise ValueError("n должно быть неотрицательным")
        return factorial(n)

    @staticmethod
    def calculate_permutations_with_repetitions(n, repeats):
        if any(k <= 0 for k in repeats):
            raise ValueError("Повторения должны быть положительными числами")
        if sum(repeats) != n:
            raise ValueError("Сумма повторений должна равняться n")
        denominator = 1
        for k in repeats:
            denominator *= factorial(k)
        return factorial(n) // denominator

    @staticmethod
    def calculate_combinations_without_repetitions(n, k):
        if n < 0 or k < 0:
            raise ValueError("Значения должны быть неотрицательными")
        if k > n:
            raise ValueError("k не может быть больше n")
        return factorial(n) // (factorial(k) * factorial(n - k))

    @staticmethod
    def calculate_combinations_with_repetitions(n, k):
        return CombinatorialModel.calculate_combinations_without_repetitions(n + k - 1, k)

    @staticmethod
    def calculate_arrangements_without_repetitions(n, k):
        if k > n:
            raise ValueError("k не может быть больше n")
        return factorial(n) // factorial(n - k)

    @staticmethod
    def calculate_arrangements_with_repetitions(n, k):
        return n ** k
