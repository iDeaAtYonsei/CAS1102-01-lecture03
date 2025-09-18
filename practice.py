from typing import List
class Shape:
    def measure(self) -> float:
        raise NotImplementedError("Subclasses must implement measure()")
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def measure(self) -> float:
        PI = 3.141592653589793
        return PI * (self.radius ** 2)
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def measure(self) -> float:
        return self.width * self.height
class Triangle(Shape):
    def __init__(self, p1: List[float], p2: List[float], p3: List[float]):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def measure(self) -> float:
        def distance(a: List[float], b: List[float]) -> float:
                return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
        a = distance(self.p1, self.p2)
        b = distance(self.p2, self.p3)
        c = distance(self.p3, self.p1)

        s = (a + b + c) / 2.0
        area_sq = s * (s - a) * (s - b) * (s - c)
        return (area_sq ** 0.5)
if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
