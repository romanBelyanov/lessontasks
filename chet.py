lst_ = []
def func(lst, x=0):
    if lst != []:
        if lst[x] % 2 == 0:
            lst_.append(lst[x])
        if x + 1 > len(lst):
            func(lst, x+1)
    return lst_

for i in func(list(map(int, input().split()))):
    print(i, end=" ")