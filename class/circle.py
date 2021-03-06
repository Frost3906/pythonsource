import math


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.__radius

    def get_circleArea(self):
        return math.pi * (self.__radius ** 2)

    def get_radius(self):  # getter
        return self.__radius

    def set_radius(self, value):  # setter
        self.__radius = value


circle = Circle(10)
print("원의 둘레", circle.get_circumference())
print("원의 면적", circle.get_circleArea())

print(circle.set_radius(15))
print("원의 둘레", circle.get_circumference())
print("원의 면적", circle.get_circleArea())
print(circle.get_radius())

