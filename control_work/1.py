class Animal:
    def make_sound(self):
        print("Животное издаёт звук")

class Dog(Animal):
    def make_sound(self):
        print("Собака лает")

class Cat(Animal):
    def make_sound(self):
        print("Кошка мяукает")