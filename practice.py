from typing import List
import math


class Shape:
    # TODO: Define the method "measure".
    def measure(self):
        raise NotImplementedError("Subclasses must implement this method.")
    """
    - This is an abstract method, so it should just raise NotImplementedError.
    """


# TODO: Create a Circle class that inherits from Shape.
# - Initialize it with a radius (float).
# - Implement the measure method to return the area of the circle.
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def measure(self):
        return math.pi * (self.radius ** 2)


# TODO: Create a Rectangle class that inherits from Shape.
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def measure(self):
        return self.width * self.height


# TODO: Create a Triangle class that inherits from Shape.
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.
class Triangle(Shape):
    def __init__(self, p1: tuple, p2: tuple, p3: tuple):
        self.v1 = p1
        self.v2 = p2
        self.v3 = p3

    def measure(self):
        # 세 변의 길이 구하기
        a = math.dist(self.v1, self.v2)
        b = math.dist(self.v2, self.v3)
        c = math.dist(self.v3, self.v1)

        # 헤론의 공식 사용
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area


if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
