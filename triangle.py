from math import sin
def triangle_(a, B, C):
    A = 180-(B+C)
    return A, a * sin(B)/sin(A), a * sin(C)/sin(A)

A, b, c = triangle_(int(input()), int(input()), int(input()))
print(A, b, c, sep="\n")