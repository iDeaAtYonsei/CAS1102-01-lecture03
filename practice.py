from typing import List
import math as mt


class Shape:
    # TODO: Define the method "measure".
    """
    - This is an abstract method, so it should just raise NotImplementedError.
    """
    raise NotImplementedError("Subclass must implement measure() method")

# TODO: Create a Circle class that inherits from Shape.
# - Initialize it with a radius (float).
# - Implement the measure method to return the area of the circle.
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def measure(self) -> float:
        return mt.pi * r * r

# TODO: Create a Rectangle class that inherits from Shape.
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.
class Rectnagle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def measure(self) -> float:
        return self.width * self.height


# TODO: Create a Triangle class that inherits from Shape.
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.
class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def measure(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return mt.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))



if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
