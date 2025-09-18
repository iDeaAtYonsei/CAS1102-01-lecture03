from typing import List
import math

class Shape:
    def measure(self):
        raise NotImplementedError
    # TODO: Define the method "measure".
    """
    - This is an abstract method, so it should just raise NotImplementedError.
    """

class Circle(Shape):
    def __init__(self, radius: float):
            self.radius=radius
    def measure(self):
        return math.pi*(self.radius**2)

class Rectangle(Shape):
    def __init__(self, width:float, height:float):
        self.width=width
        self.height=height
    def measure(self):
        return self.width*self.height

class Triangle(Shape):
    def __init__(self, p1: tuple[float, float], p2: tuple[float, float], p3: tuple[float, float]):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def measure(self):
        a = math.dist(self.p1, self.p2)
        b = math.dist(self.p2, self.p3)
        c = math.dist(self.p3, self.p1)
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

        
# TODO: Create a Circle class that inherits from Shape.
# - Initialize it with a radius (float).
# - Implement the measure method to return the area of the circle.


# TODO: Create a Rectangle class that inherits from Shape.
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.


# TODO: Create a Triangle class that inherits from Shape.
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.


if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
