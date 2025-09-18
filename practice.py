import math
from typing import List


class Shape:
    # TODO: Define the method "measure".
    """
    - This is an abstract method, so it should just raise NotImplementedError.
    """

    """
    Abstract base class for shapes.
    All shapes must implement the measure() method.
    """
    def measure(self) -> float:
        raise NotImplementedError("Subclass must implement this method")


# TODO: Create a Circle class that inherits from Shape.
# - Initialize it with a radius (float).
# - Implement the measure method to return the area of the circle.
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def measure(self) -> float:
        return math.pi * (self.radius ** 2)

# TODO: Create a Rectangle class that inherits from Shape.
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def measure(self) -> float:
        return self.width * self.height

# TODO: Create a Triangle class that inherits from Shape.
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.
class Triangle(Shape):
    def __init__(self, p1: tuple, p2: tuple, p3: tuple):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def measure(self) -> float:
        # 거리 계산 함수
        def distance(a, b):
            return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

        # 변의 길이
        a = distance(self.p1, self.p2)
        b = distance(self.p2, self.p3)
        c = distance(self.p3, self.p1)

        # 헤론의 공식
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
