from typing import List
import math

class Shape:
    # TODO: Define the method "measure".
    """
    - This is an abstract method, so it should just raise NotImplementedError.
    """
    def measure():
        pass


# TODO: Create a Circle class that inherits from Shape.
# - Initialize it with a radius (float).
# - Implement the measure method to return the area of the circle.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def measure(self):
        return pi * self.radius ** 2


# TODO: Create a Rectangle class that inherits from Shape.
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.
class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def measure(self):
        return self.w * self.h


# TODO: Create a Triangle class that inherits from Shape.
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = (x1, y1)
        self.b = (x2, y2)
        self.c = (x3, y3)

    def measure(self):
        A = math.sqrt((self.a[0] - self.b[0]) ** 2 + (self.a[1] - self.b[1]) ** 2)
        B = math.sqrt((self.b[0] - self.c[0]) ** 2 + (self.b[1] - self.c[1]) ** 2)
        C = math.sqrt((self.c[0] - self.a[0]) ** 2 + (self.c[1] - self.a[1]) ** 2)
        s = (A + B + C) / 2
        return math.sqrt(s * (s - A) * (s - B) * (s - C))
        


if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
