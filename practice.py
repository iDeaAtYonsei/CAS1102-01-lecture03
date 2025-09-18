from typing import List

import math


class Shape:
    # TODO: Define the method "measure".
    """
    - This is an abstract method, so it should just raise NotImplementedError.
    """
    def measure(self):
        raise NotImplementedError


# TODO: Create a Circle class that inherits from Shape.
# - Initialize it with a radius (float).
# - Implement the measure method to return the area of the circle.
class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, value):
        self.__radius = float(value)

    def measure(self):
        return math.pi * (Circle.get_radius(self)**2)


# TODO: Create a Rectangle class that inherits from Shape.
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.
class Rectangle(Shape):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, value):
        self.__width = float(value)

    def get_height(self):
        return self.__height

    def set_height(self, value):
        self.__height = float(value)

    def measure(self):
        w = Rectangle.get_width(self)
        h = Rectangle.get_height(self)
        return w * h

# TODO: Create a Triangle class that inherits from Shape.
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.
class Triangle(Shape):

    def __init__(self, p1, p2, p3):
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3

    def get_p1(self):
        return self.__p1

    def set_p1(self, value):
        self.__p1 = tuple(value)

    def get_p2(self):
        return self.__p2

    def set_p2(self, value):
        self.__p2 = tuple(value)

    def get_p3(self):
        return self.__p3

    def set_p3(self, value):
        self.__p3 = tuple(value)

    def measure(self):
        x1 = Triangle.get_p1(self)[0]
        x2 = Triangle.get_p2(self)[0]
        x3 = Triangle.get_p3(self)[0]
        y1 = Triangle.get_p1(self)[1]
        y2 = Triangle.get_p2(self)[1]
        y3 = Triangle.get_p3(self)[1]
        a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        b = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
        c = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
        s = (a + b + c) / 2
        return (s * (s-a) * (s-b) * (s-c)) ** 0.5


if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
