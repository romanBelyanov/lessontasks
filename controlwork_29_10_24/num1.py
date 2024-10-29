# Задача 1
# Данную задачу наиболее удобно решить с помощью цикла for, так как список lst - это глобальная переменная и использование рекурсии вызовет осложнения
import random

lst = [random.randint(1, 1000) for i in range(10)]

print("Изначальный список:", end=" ")
for i in range(len(lst)):
    if i == len(lst) - 1:
        print(f"{lst[i]}.")
    else:
        print(f"{lst[i]},", end=" ")
def summ():
    global lst
    summ_ = 0

    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            summ_ += lst[i]

    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            lst[i] = summ_

    print(f"Сумма нечётных элементов: {summ_}.")

summ()

print("Конечный список:", end=" ")
for i in range(len(lst)):
    if i == len(lst) - 1:
        print(f"{lst[i]}.")
    else:
        print(f"{lst[i]},", end=" ")