res = 0
def quest(num, _2n=1):
    global res
    if num == _2n:
        res = "YES"
    elif num < _2n:
        res = "NO"
    else:
        quest(num, _2n*2)
quest(int(input()))
print(res)