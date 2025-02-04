import time
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res_i, cnt_i = 0, 0
res_j = 0
run = True
start = time.perf_counter()
while run:
    print(array)
    # 1 пункт
    for i in range(len(array)-1, 0, -1):
        if array[i] > array[i-1]:
            res_i = i-1
            cnt_i = 0
            break
        else:
            cnt_i += 1
    if cnt_i == len(array)-1:
        run = False
    # 2 пункт
    for j in range(len(array)-1, -1, -1):
        if array[j] > array[res_i]:
            res_j = j
            break
    # 3 пункт
    array[res_i], array[res_j] = array[res_j], array[res_i]
    # 4 пункт
    array[res_i+1:] = array[res_i+1:][::-1]
end = time.perf_counter()
print(f"Время выполнения: {end-start}")


# def permutations(lst, start=0):
#    if start == len(lst) - 1:
#        print(lst)
#    else:
#        for i in range(start, len(lst)):
#            lst[start], lst[i] = lst[i], lst[start]
#            permutations(lst, start + 1)
#            lst[start], lst[i] = lst[i], lst[start]

# now_time = time.time()
# permutations(array)
# finish_time = time.time()
# print(finish_time - now_time)
