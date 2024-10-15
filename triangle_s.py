triangle1 = [[10, 5], [254, 65], [7635, 8474]]
triangle2 = [[15, 30], [200, 0], [8000, 9000]]
def line(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
triangle1_line = [line(triangle1[0][0], triangle1[0][1], triangle1[1][0], triangle1[1][1]), line(triangle1[2][0], triangle1[2][1], triangle1[1][0], triangle1[1][1]), line(triangle1[0][0], triangle1[0][1], triangle1[2][0], triangle1[2][1])]
triangle2_line = [line(triangle2[0][0], triangle2[0][1], triangle2[1][0], triangle2[1][1]), line(triangle2[2][0], triangle2[2][1], triangle2[1][0], triangle2[1][1]), line(triangle2[0][0], triangle2[0][1], triangle2[2][0], triangle2[2][1])]
def find_S_trian(a, b, c):
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5
triangle1_S = round(find_S_trian(triangle1_line[0], triangle1_line[1], triangle1_line[2]), 1)
triangle2_S = round(find_S_trian(triangle2_line[0], triangle2_line[1], triangle2_line[2]), 1)
print(f"Площадь первого треугольника: {triangle1_S}")
print(f"Площадь второго треугольника: {triangle2_S}")
if triangle1_S > triangle2_S:
    print("Площадь первого треугольника больше второго")
elif triangle1_S < triangle2_S:
    print("Площадь второго треугольника больше первого")
else:
    print("Площади треугольников равны")