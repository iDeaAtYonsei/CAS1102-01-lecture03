from typing import List


class Shape:
    # TODO: Define the method "measure".
    def measure(self):
        """
        - This is an abstract method, so it should just raise NotImplementedError.
        """
        raise NotImplementedError

# TODO: Create a Circle class that inherits from Shape.
import math

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def measure(self) -> float:
        return (self.radius ** 2) * math.pi



# - Initialize it with a radius (float).
# - Implement the measure method to return the area of the circle.


# TODO: Create a Rectangle class that inherits from Shape.
class Rectangle(Shape):
    def __init__(self, height:float, width:float):
        self.height = height
        self.width = width

    def measure(self) -> float:
        return self.width * self.height
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.


# TODO: Create a Triangle class that inherits from Shape.
class Triangle(Shape):
    def __init__(self, p1: tuple[float, float], p2: tuple[float, float], p3: tuple[float, float]):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    
    def _calculate_distance(self, vertex1: tuple[float, float], vertex2: tuple[float, float]) -> float:
        return math.sqrt((vertex2[0] - vertex1[0]) ** 2 + (vertex2[1] - vertex1[1]) ** 2)

    def measure(self) -> float:
        a = self._calculate_distance(self.p1, self.p2)
        b = self._calculate_distance(self.p2, self.p3)
        c = self._calculate_distance(self.p3, self.p1)

        sp = (a + b + c) / 2

        area_squared = sp * (sp - a) * (sp - b) * (sp - c)

        if area_squared < 0:
            return 0.0

        return math.sqrt(area_squared)
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.


if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
