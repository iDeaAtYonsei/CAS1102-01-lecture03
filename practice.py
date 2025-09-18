from typing import List
import math
pi = math.pi

class Shape:
    # TODO: Define the method "measure".
    def measure(self):
        raise NotImplementedError
    """
    - This is an abstract method, so it should just raise NotImplementedError.
    """


# TODO: Create a Circle class that inherits from Shape.
# - Initialize it with a radius (float).
# - Implement the measure method to return the area of the circle.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = float(radius)
    def measure(self):
        area = self.radius **2 * pi
        return area

# TODO: Create a Rectangle class that inherits from Shape.
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)
    def measure(self):
        area = self.width * self.height
        return area


# TODO: Create a Triangle class that inherits from Shape.
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.

class Triangle(Shape):
    def __init__(self, p1, p2, p3):
        self.p1_x = float(p1[0])
        self.p1_y = float(p1[1])
        self.p2_x = float(p2[0])
        self.p2_y = float(p2[1])
        self.p3_x = float(p3[0])
        self.p3_y = float(p3[1])
        self.a = ((self.p1_x - self.p2_x) ** 2 + (self.p1_y - self.p2_y) ** 2) ** 0.5
        self.b = ((self.p2_y - self.p3_y) ** 2 + (self.p2_y - self.p3_y) ** 2) ** 0.5
        self.c = ((self.p3_x - self.p1_x) ** 2 + (self.p3_y - self.p1_y) ** 2) ** 0.5

    def measure(self):
        s = (self.a + self.b + self.c) / 2
        area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** (1/2)
        return area


if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
