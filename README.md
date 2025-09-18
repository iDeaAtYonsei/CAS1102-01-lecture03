from typing import List, Tuple
import math


class Shape:
    def measure(self) -> float:
        """
        计算图形面积。
        这是一个抽象方法，子类必须实现。
        """
        raise NotImplementedError("Subclasses must implement measure().")


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def measure(self) -> float:
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def measure(self) -> float:
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, p1: Tuple[float, float], p2: Tuple[float, float], p3: Tuple[float, float]):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def measure(self) -> float:
        def dist(a, b):
            return math.hypot(a[0] - b[0], a[1] - b[1])

        a = dist(self.p1, self.p2)
        b = dist(self.p2, self.p3)
        c = dist(self.p3, self.p1)

        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
