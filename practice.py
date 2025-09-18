from typing import List, Tuple
import math


class Shape:
    # Abstract method
    def measure(self) -> float:
        """
        Abstract method to compute the area of the shape.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method")


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def measure(self) -> float:
        return math.pi * (self.radius ** 2)


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
        # 거리 계산 함수
        def distance(a: Tuple[float, float], b: Tuple[float, float]) -> float:
            return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

        # 변의 길이
        a = distance(self.p1, self.p2)
        b = distance(self.p2, self.p3)
        c = distance(self.p3, self.p1)

        # Heron's formula
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
