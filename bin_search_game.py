import random
num1 = 0

def binary_search(data, elem):
    low = 0
    high = len(data) - 1

    while low <= high:
        middle = (low + high) // 2
        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1

    return "Нужно вводить число из заданного диапазона"


def game():
    from_num = random.choice([i * 10 for i in range(1, 11)])
    to_num = random.choice([i * 1000 for i in range(1, 11)])
    lst = [i for i in range(from_num, to_num+1)]
    num = random.randint(from_num, to_num)

    print(f"Я загадал число от {from_num} до {to_num}")
    print("Ты пиши число, а я буду говорить, больше или меньше оно загаданного числа или ты угадал")

    def trying():
        try:
            global num1
            num1 = int(input("Напиши число: "))
        except:
            print("Вводить нужно числа")
            trying()
    trying()

    cnt = 0
    while num1 != num:
        try:
            if binary_search(lst, num1) > lst.index(num):
                print("Моё число меньше")
            elif binary_search(lst, num1) < lst.index(num):
                print("Моё число больше")
            cnt += 1
        except:
            print(binary_search(lst, num1))

        def trying():
            try:
                global num1
                num1 = int(input("Напиши число: "))
            except:
                print("Вводить нужно числа")
                trying()
        trying()

    cnt += 1
    print(f"Поздравляю! Ты угадал. Тебе понадобилось {cnt} попыток")

    new_game = input("Будешь играть ещё раз?")
    if new_game.lower() == "yes" or new_game.lower() == "да" or new_game.lower() == "1":
        game()


game()