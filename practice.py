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
        pass
        
# TODO: Create a Circle class that inherits from Shape.
# - Initialize it with a radius (float).
# - Implement the measure method to return the area of the circle.
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = float(radius)

    def measure(self):
        return math.pi * (self.radius)**2
        
# TODO: Create a Rectangle class that inherits from Shape.
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = float(width)
        self.height = float(height)

    def measure(self):
        return self.width * self.height

# TODO: Create a Triangle class that inherits from Shape.
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.
class Triangle(Shape):
    def __init__(self, p1: tuple, p2: tuple, p3: tuple):
        self.d1 = math.sqrt((p3[0] - p2[0])**2 + (p3[1] - p2[1])**2)
        self.d2 = math.sqrt((p3[0] - p1[0])**2 + (p3[1] - p2[1])**2)
        self.d3 = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
        self.s = (self.d1 + self.d2 + self.d3)/2

    def measure(self):
        return math.sqrt(self.s(self.s - self.d1)(self.s - self.d2)(self.s - self.d3))


if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
