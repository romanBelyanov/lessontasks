import math
task1 = int(input("Введите сторону квадрата: "))
print(f"Площадь квадрата со стороной {task1} равна {task1**2}")
task2 = list(map(int, input("Введите стороны прямоугольника через пробел: ").split()))
print(f"Периметр прямоугольника со сторонами {task2[0]} и {task2[1]} равна {2*(task2[0]+task2[1])}")
task3 = int(input("Введите радиус круга: "))
print(f"Площадь круга с радиусом {task3} равна {task3**2*math.pi}")
