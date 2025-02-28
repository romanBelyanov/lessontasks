lst = ["Математика", "Информатика", "Русский язык"]
elements = []
def permutations(lst, start=0):
    if start == len(lst) - 1:
        elements.append(lst[:-1])
        return
    else:
        for i in range(start, len(lst)):
            lst[start], lst[i] = lst[i], lst[start]
            permutations(lst, start + 1)
            lst[start], lst[i] = lst[i], lst[start]
elements.extend([[i] * 2 for i in lst])
permutations(lst)
print(elements)