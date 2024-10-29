# В этой задаче было легче всего использовать рекурсию, так как нельзя узнать, в какой момент нужно остановиться, без рекурсии
res = 0
def quest(num, _2n=1, i=0):
    global res
    if num == _2n:
        res = f"YES, 2**{i}={num}"
        return
    elif num < _2n:
        res = "NO"
        return
    else:
        quest(num, _2n*2, i+1)
quest(int(input()))
print(res)
