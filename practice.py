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
        raise NotImplementedError
    


# TODO: Create a Circle class that inherits from Shape.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = float(radius)

    def measure(self):
        area = math.pi * self.radius**2
        return area
# - Initialize it with a radius (float).
# - Implement the measure method to return the area of the circle.


# TODO: Create a Rectangle class that inherits from Shape.
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    def measure(self):
        area = self.width * self.height
        return area
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.


# TODO: Create a Triangle class that inherits from Shape.
class Triangle(Shape):
    def __init__(self, p1, p2, p3):
        self.a = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1]))
        self.b = math.sqrt((p2[0]-p3[0])**2 + (p2[1]-p3[1]))
        self.c = math.sqrt((p3[0]-p1[0])**2 + (p3[1]-p1[1]))
        self.s = (self.a + self.b + self.c) / 2

    def measure(self):
        area = math.sqrt(self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c))
        return area
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.


if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
