# В данной задаче было удобно использовать 2 функции: для нахождения длины отрезка по координатам вершин и для нахождения периметра по длинам сторон, так как функцию для нахождения длины отрезка нужно было использовать 3 раза
def line(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def find_P_trian(a, b, c):
    return a+b+c

triangle = [[float(input(f"Введите координату X {i+1} вершины: ")), float(input(f"Введите координату Y {i+1} вершины: "))] for i in range(3)]
triangle1_line = [line(triangle[0][0], triangle[0][1], triangle[1][0], triangle[1][1]), line(triangle[2][0], triangle[2][1], triangle[1][0], triangle[1][1]), line(triangle[0][0], triangle[0][1], triangle[2][0], triangle[2][1])]

triangle1_P = round(find_P_trian(triangle1_line[0], triangle1_line[1], triangle1_line[2]), 1)
print(f"Периметр треугольника: {triangle1_P}")