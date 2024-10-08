# Контрольная работа, уровень С, Белянов Роман Антонович, ИИ-71, задание 1
lst = []
summ = 0


def trying():
    try:
        global lst
        lst = list(map(int, input("Введите числа через пробел: ").split()))
    except:
        print("Вводить нужно числа")
        trying()
trying()

for i in range(len(lst)):
    if lst[i] > 0:
        summ += lst[i]

print(f"Сумма положительных чисел в списке {lst} равна {summ}")