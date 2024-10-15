a = int(input())
b = int(input())
res = 0
def nod(a, b):
    global res
    if a < b:
        a, b = b, a
    elif a == b:
        res = a
        return a
    a = a - b
    nod(a, b)
nod(a, b)
print(res)