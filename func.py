def f(x):
    if -2 <= x < 2:
        return x ** 2
    elif x >= 2:
        return x ** 2 + 4 * x + 5
    else:
        return 4
print(f(int(input())))