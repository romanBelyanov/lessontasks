import itertools as it

#--------------------------------------------------
print(list(it.combinations(["A", "B", "Г"], 2)))
#--------------------------------------------------
print(list(it.combinations(["A", "Б", "B", "Г"], 3)))
#--------------------------------------------------
print(list(it.combinations(["A", "Б", "B", "Г", "Д", "Е", "Ж"], 2)))
#--------------------------------------------------
books = list(it.combinations(["К1", "К2", "К3", "К4", "К5", "К6", "К7", "К8", "К8", "К10"], 3))
magazines = list(it.combinations(["Ж1", "Ж2", "Ж3", "Ж4"], 2))
for i in books:
    for j in magazines:
        print(f"{i}{j}")
