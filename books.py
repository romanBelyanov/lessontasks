description = "0 - Завершить программу и сохранить все мои книги\n1 - Вывести список моих книг\n2 - Добавить книгу\n3 - Удалить выбранную книгу\n4 - Удалить все книги\nВведите число для выполнения дествия: "
try:
    with open("library.docx", "r") as file:
        between = list(map(str, file.read().split("\nyears\n")))
        books = between[0]
        books = list(books.split(", "))
        if books == [""]:
            books = []
            years = []
        else:
            years = between[1]
            years = list(map(int, years.split(", ")))
        del between
        file.close()
except:
    with open("library.docx", "w") as file:
        file.close()
        books = []
        years = []
def print_books(books, years):
    with open("library.docx", "w") as file:
        for i in range(len(books)):
            file.write(books[i])
            if i == len(books)-1:
                pass
            else:
                file.write(", ")
        file.write("\nyears\n")
        for i in range(len(years)):
            file.write(str(years[i]))
            if i == len(years)-1:
                pass
            else:
                file.write(", ")
        file.close()
    if len(books) != 0:
        print("Ваш список книг: ", end="")
        for i in range(len(books)):
            if i == len(books)-1:
                if i == 0:
                    print(f"{books[i]} {years[i]} года издания", end=".\n")
                else:
                    print(f"                 {books[i]} {years[i]} года издания", end=".\n")
            else:
                if i == 0:
                    print(f"{books[i]} {years[i]} года издания", end=",\n")
                else:
                    print(f"                 {books[i]} {years[i]} года издания", end=",\n")
    else:
        print("Ваш список книг пуст")


def append_book(books, book, years, year):
    years.append(year)
    years.sort()
    books.insert(years.index(year), book)
    print(f"Книга {book} {year} года издания успешно добавлена")
    print_books(books, years)
    return books, years

def delete_book(books, book, years):
    try:
        books.pop(books.index(book))
        years.pop(books.index(book))
        print(f"Книга {book} успешно удалена")
    except:
        print(f"Книги {book} нет")
    print_books(books, years)
    return books, years

def delete_all_books(books, years):
    books.clear()
    print("Все книги успешно удалены")
    print_books(books, years)
    return books

def menu(num, books, years, description):
    if num == 0:
        exit(0)
    elif num == 1:
        print_books(books, years)
    elif num == 2:
        try:
            books, years = append_book(books, input("Введите название книги: "), years, int(input("Введите год издания книги: ")))
        except:
            print("Год - целое число")
            menu(num, books, years)
    elif num == 3:
        books, years = delete_book(books, input("Введите название книги: "), years)
    elif num == 4:
        delete_all_books(books, years)
        books = []
        years = []
    menu(int(input(description)), books, years, description)

menu(int(input(description)), books, years, description)
