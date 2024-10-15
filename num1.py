def exchange(cost, summ):
    if cost >= 0 and summ >= 0:
        return summ / cost
    else:
        return ("Валюта не может быть отрицательной или равной нулю")
print(exchange(float(input("Валюта: ")), float(input("Кол-во рублей: "))))