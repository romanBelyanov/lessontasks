books = []
def print_books(*books):
    books = books[0]
    if len(books) != 0:
        print("Ваш список книг: ", end="")
        for i in range(len(books)):
            if i == len(books)-1:
                print(books[i], end=".\n")
            else:
                print(books[i], end=", ")
    else:
        print("Ваш список книг пуст")

def append_book(*books, book):
    books = books[0]
    books = list(books)
    books.append(book)
    print(f"Книга {book} успешно добавлена")
    print_books(books)
    return books

def delete_books(*books, book):
    books = books[0]
    books = list(books)
    try:
        books.pop(books.index(book))
        print(f"Книга {book} успешно удалена")
    except:
        print("Такой книги нет")
    print_books(books)
    return books

def delete_all_books(*books):
    books = list(books[0])
    books.clear()
    print("Все книги успешно удалены")
    print_books(books)
    return books

books = append_book(books, book="livre")
books = append_book(books, book="grand")
books = delete_books(books, book="grands")
books = delete_all_books(books)