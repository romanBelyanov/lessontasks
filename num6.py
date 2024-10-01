import random
x = int(input())
y = int(input())

matrix = [[random.randint(1,10)for i in range(x)] for j in range(y)]
for row in matrix:
    for element in row:
        print(element, end='\t')
    print()