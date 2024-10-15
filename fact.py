res = 1
def factorial(n):
    global res
    if n > 0:
        res *= n
        factorial(n-1)
factorial(int(input()))
print(res)
