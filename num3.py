lst = list(map(int, input().split()))
res = [0 for i in range(max(lst)+1)]
for i in range(len(lst)):
    res[lst.index(lst[i])] = lst.count(lst[i])
print(res)