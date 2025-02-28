elements = []
def permutations(lst, start=0):
   if start == len(lst) - 1:
       elements.append("".join(lst[:-1]))
       return
   else:
       for i in range(start, len(lst)):
           lst[start], lst[i] = lst[i], lst[start]
           permutations(lst, start + 1)
           lst[start], lst[i] = lst[i], lst[start]
permutations(["1", "2", "3", "4"])
print(len(list(set(elements))))