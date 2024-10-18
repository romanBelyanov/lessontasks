def print_n(x, n):
    if x == n:
        print(x)
        return
    print(x)
    if x < n:
        print_n(x+1, n)
    else:
        print_n(x-1, n)
print_n(1, int(input()))