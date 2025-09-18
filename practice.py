import math
from typing import List, Tuple


class Shape:
    """
    Base class for geometric shapes
    """
    # TODO: Define the method "measure".
    def measure(self) -> float:
        """
        Abstract method to be implemented by subclasses.
        It raises a NotImplementedError.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")

# TODO: Create a Circle class that inherits from Shape.
# - Initialize it with a radius (float).
# - Implement the measure method to return the area of the circle.
class Circle(Shape):
    """
    A class for circles, inheriting from Shape.
    """
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def measure(self) -> float:
        """
        Calculates the area of the circle.
        """
        return math.pi * self.radius ** 2

# TODO: Create a Rectangle class that inherits from Shape.
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.
class Rectangle(Shape):
    """
    A class for rectangles, inheriting from Shape.
    """
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.width = width
        self.height = height

    def measure(self) -> float:
        """
        Calculates the area of the rectangle.
        """
        return self.width * self.height

# TODO: Create a Triangle class that inherits from Shape.
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.
class Triangle(Shape):
    """
    A class for triangles, inheriting from Shape.
    It uses Heron's formula to calculate the area from three vertices.
    """
    def __init__(self, p1: Tuple[float, float], p2: Tuple[float, float], p3: Tuple[float, float]):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def _distance(self, p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
        """
        Helper method to calculate the distance between two points.
        """
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

    def measure(self) -> float:
        """
        Calculates the area of the triangle using Heron's formula.
        """
        # Calculate the lengths of the sides of the triangle
        a = self._distance(self.p1, self.p2)
        b = self._distance(self.p2, self.p3)
        c = self._distance(self.p3, self.p1)

        # Check for degenerate triangles (three points on a line)
        if a + b <= c or a + c <= b or b + c <= a:
            return 0.0

        # Calculate the semi-perimeter
        s = (a + b + c) / 2

        # Apply Heron's formula
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area

if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])


