def input_rectangle():
    weight = int(input())
    longth = int(input())
    return weight, longth
def input_circle():
    rad = int(input())
    return rad
def input_triangle():
    a = int(input())
    b = int(input())
    c = int(input())
    return a, b, c
def input_rhomb():
    dia1 = int(input())
    dia2 = int(input())
    return dia1, dia2
def find_S_rect(weight, longth):
    print(weight*longth)
def find_S_circle(rad):
    print(3.14159*rad**2)
def find_S_trian(a, b, c):
    p = (a+b+c)/2
    print((p*(p-a)*(p-b)*(p-c))**0.5)
def find_S_rhomb(dia1, dia2):
    print(dia1*dia2/2)
def find_P_rect(weight, longth):
    print(2*(weight+longth))
def find_P_circle(rad):
    print(3.14159*rad*2)
def find_P_trian(a, b, c):
    print(a+b+c)
def find_P_rhomb(dia1, dia2):
    print(4*(((dia1/2)**2+(dia2/2)**2))**0.5)

weight, longth = input_rectangle()
find_S_rect(weight, longth)
find_P_rect(weight, longth)
rad = input_circle()
find_S_circle(rad)
find_P_circle(rad)
a, b, c = input_triangle()
find_S_trian(a, b, c)
find_P_trian(a, b, c)
dia1, dia2 = input_rhomb()
find_S_rhomb(dia1, dia2)
find_P_rhomb(dia1, dia2)