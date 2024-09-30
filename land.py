import random
i1 = 0
j1 = 0
x = int(input())
y = int(input())
all_land = [
    [0 for i in range(x)] for j in range(y)
]
for i in range(y):
    for j in range(x):
        if i == 0 or j == 0 or j == x-1 or i == y-1:
            continue
        else:
            all_land[i][j] = random.choice([1, 1, 1, 0])

for i in range(y):
    for j in range(x):
        if i == 0 or j == 0 or j == x-1 or i == y-1:
            continue
        else:
            if all_land[i][j] == 1 and all_land[i-1][j] == 0 and all_land[i+1][j] == 0 and all_land[i][j-1] == 0 and all_land[i][j+1] == 0:
                all_land[i][j] = 0
old = 0
new = -1
for z in range((x+y)//2):
    for i in range(y):
        for j in range(x):
            if all_land[i][j] == old:
                if i == 0:
                    if j == 0:
                        if all_land[i+1][j] <= old and all_land[i][j+1] <= old:
                            all_land[i][j] = new
                    elif j == x-1:
                        if all_land[i + 1][j] <= old and all_land[i][j - 1] <= old:
                            all_land[i][j] = new
                    else:
                        if all_land[i][j-1] <= old and all_land[i][j+1] <= old and all_land[i+1][j] <= old:
                            all_land[i][j] = new
                if i == y-1:
                    if j == 0:
                        if all_land[i - 1][j] <= old and all_land[i][j + 1] <= old:
                            all_land[i][j] = new
                    elif j == x-1:
                        if all_land[i - 1][j] <= old and all_land[i][j - 1] <= old:
                            all_land[i][j] = new
                    else:
                        if all_land[i][j-1] <= old and all_land[i][j+1] <= old and all_land[i-1][j] <= old:
                            all_land[i][j] = new
                else:
                    if j == 0:
                        if all_land[i+1][j] <= old and all_land[i-1][j] <= old and all_land[i][j+1] <= old:
                            all_land[i][j] = new
                    elif j == x - 1:
                        if all_land[i+1][j] <= old and all_land[i-1][j] <= old and all_land[i][j-1] <= old:
                            all_land[i][j] = new
                    else:
                        if all_land[i][j-1] <= old and all_land[i][j+1] <= old and all_land[i+1][j] <= old and all_land[i-1][j] <= old:
                            all_land[i][j] = new
    old -= 1
    new -= 1

old = 1
new = 2
for z in range((x+y)//2):
    for i in range(y):
        for j in range(x):
            if all_land[i][j] == old:
                if i == 0:
                    if j == 0:
                        if all_land[i+1][j] >= old and all_land[i][j+1] >= old:
                            all_land[i][j] = new
                    elif j == x-1:
                        if all_land[i + 1][j] >= old and all_land[i][j - 1] >= old:
                            all_land[i][j] = new
                    else:
                        if all_land[i][j-1] >= old and all_land[i][j+1] >= old and all_land[i+1][j] >= old:
                            all_land[i][j] = new
                if i == y-1:
                    if j == 0:
                        if all_land[i - 1][j] >= old and all_land[i][j + 1] >= old:
                            all_land[i][j] = new
                    elif j == x-1:
                        if all_land[i - 1][j] >= old and all_land[i][j - 1] >= old:
                            all_land[i][j] = new
                    else:
                        if all_land[i][j-1] >= old and all_land[i][j+1] >= old and all_land[i-1][j] >= old:
                            all_land[i][j] = new
                else:
                    if j == 0:
                        if all_land[i+1][j] >= old and all_land[i-1][j] >= old and all_land[i][j+1] >= old:
                            all_land[i][j] = new
                    elif j == x - 1:
                        if all_land[i+1][j] >= old and all_land[i-1][j] >= old and all_land[i][j-1] >= old:
                            all_land[i][j] = new
                    else:
                        if all_land[i][j-1] >= old and all_land[i][j+1] >= old and all_land[i+1][j] >= old and all_land[i-1][j] >= old:
                            all_land[i][j] = new
    old += 1
    new += 1

for i in range(x*y//10):
    for i in range(y):
        for j in range(x):
            if all_land[i][j] >= 3:
                i1 = i
                j1 = j
                break
        if all_land[i1][j1] >= 3:
            break
    while all_land[i1][j1] != 0:
        a = random.choice([-1, 1])
        b = random.choice([-1, 1])
        i1 = i1 + a
        all_land[i1 - a][j1] = 0
        j1 = j1 + b
        all_land[i1][j1 - b] = 0


for i in all_land:
    for j in i:
        if j < 0:
            print(j, end=" ")
        else:
            print("", j, end=" ")
    print()
