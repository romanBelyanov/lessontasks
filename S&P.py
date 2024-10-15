def input_rectangle():
    global weight, longth
    weight = int(input())
    longth = int(input())
def input_circle():
    global rad
    rad = int(input())
def input_triangle():
    global a, b, c
    a = int(input())
    b = int(input())
    c = int(input())
def input_rhomb():
    global dia1, dia2
    dia1 = int(input())
    dia2 = int(input())
def find_S_rect():
    input_rectangle()
    print(weight*longth)
def find_S_circle():
    input_circle()
    print(3.14159*rad**2)
def find_S_trian():
    input_triangle()
    p = (a+b+c)/2
    print((p*(p-a)*(p-b)*(p-c))**0.5)
def find_S_rhomb():
    input_rhomb()
    print(dia1*dia2/2)
def find_P_rect():
    find_S_rect()
    print(2*(weight+longth))
def find_P_circle():
    find_S_circle()
    print(3.14159*rad*2)
def find_P_trian():
    find_S_trian()
    print(a+b+c)
def find_P_rhomb():
    find_S_rhomb()
    print(4*(((dia1/2)**2+(dia2/2)**2))**0.5)

find_P_rect()
find_P_circle()
find_P_trian()
find_P_rhomb()