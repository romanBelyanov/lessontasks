elements = [i for i in input("Введите слово для перестановки: ")]
lst = []
def permutations(elements):
    if len(elements) <= 1:
        if elements not in lst:
            yield elements
        return
    for perm in permutations(elements[1:]):
        for i in range(len(elements)):
            if perm[:i] + elements[0:1] + perm[i:] not in lst:
                yield perm[:i] + elements[0:1] + perm[i:]

def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n-1)


res = permutations(elements)
for i in range(fact(len(elements))):
    try:
        a = next(res)
        print("".join(a))
        lst.append(a)
    except:
        pass
