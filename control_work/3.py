from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def P(self):
        pass

    @abstractmethod
    def print_info(self):
        pass


class Rect(Shape):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def area(self):
        return self.a*self.b
    
    def P(self):
        return 2*(self.a+self.b)
    
    def print_info(self):
        return f"Площадь прямоугольника равна {self.area()}\nПериметр прямоугольника равен {self.P()}"
    

class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.r = r

    def area(self):
        return math.pi*self.r**2
    
    def P(self):
        return 2*math.pi*(self.r)
    
    def print_info(self):
        return f"Площадь круга равна {self.area()}\nПериметр круга равен {self.P()}"
    
area = [
    Rect(5, 10),
    Circle(5),
]
for i in area:
    print(i.print_info())
