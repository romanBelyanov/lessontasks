from abc import ABC, abstractmethod

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
    
area = Rect(5, 10)
print(area.print_info())