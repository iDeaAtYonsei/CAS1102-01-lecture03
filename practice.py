from typing import List
import math

class Shape:
    def method(self):
        """
        - This is an abstract method, so it should just raise NotImplementedError.
        """
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def measure(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def measure(self):
        return self.width * self. height

class Triangle(Shape):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def measure(self):
        def dist(a, b):
            return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
        a = dist(self.p1, self.p2)
        b = dist(self.p2, self.p3)
        c = dist(self.p3, self.p1)

        s = (a + b + c) / 2
        area = math.sqrt(s * (s-1) * (s-b) * (s-c))
        return area


if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
