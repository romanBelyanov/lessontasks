# Контрольная работа, уровень С, Белянов Роман Антонович, ИИ-71, задание 3
import random
n = 0
max = 0
min = 1000000
def trying():
    try:
        global n
        n = int(input("Введите число: "))
    except:
        print("Вводить нужно число")
        trying()
trying()
lst = [random.randint(1, 1000000) for i in range(n)]
for i in range(n):
    if lst[i] < min:
        min = lst[i]
    else:
        pass
    if lst[i] > max:
        max = lst[i]
    else:
        pass
print(f"В списке {lst} минимальным элементом является число {min}, а максимальным элементом является число {max}")