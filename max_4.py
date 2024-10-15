def max_2(a, b):
    if b > a:
        a, b = b, a
    return a
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if max_2(a, b) == b:
    a, b = b, a
else:
    pass
if max_2(a, c) == c:
    a, c = c, a
else:
    pass
if max_2(a, d) == d:
    a, d = d, a
print(a)