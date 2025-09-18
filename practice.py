from typing import List
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    # TODO: Define the method "measure".
    """
    - This is an abstract method, so it should just raise NotImplementedError.
    """
    @abstractmethod
    def measure(self):
        try:
            pass
        except:
            raise NotImplementedError


# TODO: Create a Circle class that inherits from Shape.
# - Initialize it with a radius (float).
# - Implement the measure method to return the area of the circle.
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = float(radius)
    def measure(self):
        return math.pi * (self.__radius ** 2)

# TODO: Create a Rectangle class that inherits from Shape.
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.
class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = float(width)
        self.__height = float(height)
    def measure(self):
        return self.__width * self.__height


# TODO: Create a Triangle class that inherits from Shape.
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.
class Triangle(Shape):
    def __init__(self, p1, p2, p3):
        self.__p1 = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        self.__p2 = (p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2
        self.__p3 = (p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2
    def measure(self):
        l1 = self.__p1 ** (1/2)
        l2 = self.__p2 ** (1/2)
        l3 = self.__p3 ** (1/2)
        s = (l1 + l2 + l3) / 2
        return (s * (s - l1) * (s - l2) * (s - l3)) ** (1/2)


if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
