num = 0
def trying():
    global num
    try:
        num = int(input())
    except:
        print("Вводите число")
        trying()

trying()

if num % 3 == 0:
    print(f"Число {num} делится на 3 без остатка")
else:
    print(f"Число {num} делится на 3 с остатком {num % 3}")