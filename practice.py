from typing import List
import math

class Shape:
    # TODO: Define the method "measure".
    """
    - This is an abstract method, so it should just raise NotImplementedError.
    """
    def measure(self):
        raise NotImplementedError

# TODO: Create a Circle class that inherits from Shape.
# - Initialize it with a radius (float).
# - Implement the measure method to return the area of the circle.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = float(radius)
    def measure(self):
        return self.radius*self.radius*math.pi 

# TODO: Create a Rectangle class that inherits from Shape.
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)
    def measure(self):
        return self.width*self.height

# TODO: Create a Triangle class that inherits from Shape.
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.
class Triangle(Shape):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def measure(self):
        self.side12 = ((self.p1[0] - self.p2[0])**2 + (self.p1[1] - self.p2[1])**2)**0.5
        self.side23 = ((self.p2[0] - self.p3[0])**2 + (self.p2[1] - self.p3[1])**2)**0.5
        self.side31 = ((self.p3[0] - self.p1[0])**2 + (self.p3[1] - self.p1[1])**2)**0.5
        self.s = (self.side12 + self.side23 + self.side31) / 2
        return (self.s*(self.s - self.side12)*(self.s - self.side23)*(self.s - self.side31))**0.5

if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
