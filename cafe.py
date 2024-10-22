products = ["А", "Б", "В", "Г"]
prices = [10, 20, 30, 40]
products_user = []
prices_user = []
def decor(func):
    def wrapper():
        username, password = func()
        if username == "user" and password == "123":
            user()
        elif username == "admin" and password == "unicum-adm23":
            admin()
    return wrapper

def user():
    if len(products) != 0:
        print(f"Список продуктов и цен: ", end="")
        for i in range(len(products)):
            if i != len(products) - 1:
                print(f"{i+1} - {products[i]} - {prices[i]} рублей;")
            else:
                print(f"{i+1} - {products[i]} - {prices[i]} рублей.")
        product = input(
            "Введите название продукта. Если вы хотите завершить покупку, введите \"Конец\" или \"0\": ").lower()
        if product == "конец" or product == "0":
            check()
        elif product[0].upper()+product[1:] in products:
            products_user.append(products[products.index(product[0].upper()+product[1:])])
            prices_user.append(prices[products.index(product[0].upper() + product[1:])])
            user()
        elif product in list(map(str, range(1, len(products) + 1))):
            products_user.append(products[int(product)-1])
            prices_user.append(prices[int(product)-1])
            user()
    else:
        print("Список продуктов и цен пуст")

def admin():
    if len(products) != 0:
        print(f"Список продуктов и цен: ", end="")
        for i in range(len(products)):
            if i != len(products) - 1:
                print(f"{i+1} - {products[i]} - {prices[i]} рублей;")
            else:
                print(f"{i+1} - {products[i]} - {prices[i]} рублей.")
    else:
        print("Список продуктов и цен пуст")
    product = input("Введите новый товар: ")
    price = int(input("Введите цену товара: "))
    products.append(product)
    prices.append(price)
    enter_name()


def return_cheque(func):
    def result():
        paying = func()
        cheque = ""
        if paying == "наличные":
            print(f"С вас {sum(prices_user)}")
            money = int(input("Сколько будешь платить: "))
            if money < sum(prices_user):
                print(f"Вам нужно вводить как минимум {sum(prices_user)}")
                result()
            cheque = "==============================\n"
            for i in range(len(products_user)):
                if products_user[i] in cheque:
                    continue
                cheque += f"{products_user[i]}: {prices[products.index(products_user[i])]} руб. x {products_user.count(products_user[i])} шт.\n"
            cheque += "\n"
            cheque += f"Итого к оплате: {str(sum(prices_user))} руб.\n"
            cheque += f"Внесено: {str(money)} руб.\n"
            cheque += (f"Сдача: {str(money - sum(prices_user))} руб.")
        elif paying == "безналичные":
            cheque = "==============================\n"
            for i in range(len(products_user)):
                if products_user[i] in cheque:
                    continue
                cheque += f"{products_user[i]}: {prices[products.index(products_user[i])]} руб. x {products_user.count(products_user[i])} шт.\n"
            cheque += "\n"
            cheque += f"Итого к оплате: {sum(prices_user)} руб.\n"

        with open("cheque.txt", "w") as file:
            for i in range(len(cheque)):
                file.write(cheque[i])
            file.close()
    return result
@decor
def enter_name():
    name, password = input(), input()
    return name, password

@return_cheque
def check():
    paying = input("Как вы будете оплачивать? (Наличными или безналичными): ").lower()
    if paying == "наличными":
        return "наличные"
    if paying == "безналичными":
        return "безналичные"
    else:
        print("Нормально вводите")
        check()


enter_name()