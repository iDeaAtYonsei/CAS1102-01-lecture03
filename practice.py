from typing import List, Tuple
import math


class Shape:
    # TODO: Define the method "measure".
    """
    - This is an abstract method, so it should just raise NotImplementedError.
    """
    def measure(self) -> float:
        raise NotImplementedError("Subclasses must implement measure()")


# TODO: Create a Circle class that inherits from Shape.
# - Initialize it with a radius (float).
# - Implement the measure method to return the area of the circle.
class Circle(Shape):
    def __init__(self, radius: float):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        if radius < 0:
            raise ValueError("radius must be non-negative")
        self.radius = float(radius)

    def measure(self) -> float:
        return math.pi * (self.radius ** 2)


# TODO: Create a Rectangle class that inherits from Shape.
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("width and height must be numbers")
        if width < 0 or height < 0:
            raise ValueError("width and height must be non-negative")
        self.width = float(width)
        self.height = float(height)

    def measure(self) -> float:
        return self.width * self.height


# TODO: Create a Triangle class that inherits from Shape.
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.
class Triangle(Shape):
    def __init__(self, p1: Tuple[float, float], p2: Tuple[float, float], p3: Tuple[float, float]):
        def _validate_point(p, name: str):
            if (not isinstance(p, (tuple, list)) or len(p) != 2
                    or not all(isinstance(coord, (int, float)) for coord in p)):
                raise TypeError(f"{name} must be a tuple/list of two numbers")

        _validate_point(p1, "p1")
        _validate_point(p2, "p2")
        _validate_point(p3, "p3")

        self.p1 = (float(p1[0]), float(p1[1]))
        self.p2 = (float(p2[0]), float(p2[1]))
        self.p3 = (float(p3[0]), float(p3[1]))

    def measure(self) -> float:
        def _dist(a: Tuple[float, float], b: Tuple[float, float]) -> float:
            return math.hypot(a[0] - b[0], a[1] - b[1])

        a = _dist(self.p1, self.p2)
        b = _dist(self.p2, self.p3)
        c = _dist(self.p3, self.p1)

        # semiperimeter
        s = (a + b + c) / 2.0
        # Heron's formula (guard against tiny negative due to fp error)
        area_sq = s * (s - a) * (s - b) * (s - c)
        return math.sqrt(max(area_sq, 0.0))


if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
