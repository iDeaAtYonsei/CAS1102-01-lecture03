from typing import List


class Shape:
    """
    Base class for all shapes.
    Defines an abstract measure method to be implemented by subclasses.
    """

    def measure(self) -> float:
        """
        Abstract method that calculates the area of the shape.
        Subclasses must override this method.
        """
        raise NotImplementedError("Subclasses must implement the measure() method.")


# TODO: Create a Circle class that inherits from Shape.
# - Initialize it with a radius (float).
# - Implement the measure method to return the area of the circle.
class Circle(Shape):
    """
    Circle shape class that inherits from Shape.
    """

    def __init__(self, radius: float):
        """
        Initialize a circle with a given radius.
        :param radius: Radius of the circle
        """
        self.radius = radius

    def measure(self) -> float:
        """
        Compute the area of the circle: π * r^2
        """
        return math.pi * (self.radius ** 2)


# TODO: Create a Rectangle class that inherits from Shape.
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.

class Rectangle(Shape):
    """
    Rectangle shape class that inherits from Shape.
    """

    def __init__(self, width: float, height: float):
        """
        Initialize a rectangle with given width and height.
        :param width: Width of the rectangle
        :param height: Height of the rectangle
        """
        self.width = width
        self.height = height

    def measure(self) -> float:
        """
        Compute the area of the rectangle: width * height
        """
        return self.width * self.height

# TODO: Create a Triangle class that inherits from Shape.
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.

class Triangle(Shape):
    """
    Triangle shape class that inherits from Shape.
    """

    def __init__(self, p1: Tuple[float, float], p2: Tuple[float, float], p3: Tuple[float, float]):
        """
        Initialize a triangle with three vertices.
        :param p1: First vertex (x, y)
        :param p2: Second vertex (x, y)
        :param p3: Third vertex (x, y)
        """
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def measure(self) -> float:
        """
        Compute the area of the triangle using Heron's formula.
        """
        # Distance between points
        a = math.dist(self.p1, self.p2)
        b = math.dist(self.p2, self.p3)
        c = math.dist(self.p3, self.p1)

        # Semi-perimeter
        s = (a + b + c) / 2

        # Heron's formula
        return math.sqrt(s * (s - a) * (s - b) * (s - c))



if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
