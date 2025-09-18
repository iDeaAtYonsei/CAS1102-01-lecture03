from typing import List
import math


class Shape:
    def measure(self):
        """
        - This is an abstract method, so it should just raise NotImplementedError.
        """
        raise NotImplementedError('measure() must be implemented in subclasses')


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def measure(self) -> float:
        """Return area = π * r^2"""
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def measure(self) -> float:
        """Return area = width * height"""
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, p1: tuple, p2: tuple, p3: tuple):
        self.p1 = p1  # (x1, y1)
        self.p2 = p2  # (x2, y2)
        self.p3 = p3  # (x3, y3)

    def measure(self) -> float:
        """Compute area using Heron's formula from vertex coordinates."""
        def distance(point1, point2):
            return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
        
        a = distance(self.p1, self.p2)
        b = distance(self.p2, self.p3)
        c = distance(self.p3, self.p1)

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
