from typing import List 
import math


class Shape:
    # TODO: Define the method "measure".
    def measure(self):
        """
        - This is an abstract method, so it should just raise NotImplementedError.
        """
        raise NotImplementedError

# TODO: Create a Circle class that inherits from Shape.
class Circle(Shape):
# - Initialize it with a radius (float).
    def __init__(self, radius):
        self.radius = float(radius)
        
# - Implement the measure method to return the area of the circle.
    def measure(self):
        return math.pi * self.radius ** 2

# TODO: Create a Rectangle class that inherits from Shape.
class Rectangle(Shape):
# - Initialize it with width and height (floats).
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)
# - Implement the measure method to return the area of the rectangle.
    def measure(self):
        return self.width * self.height

# TODO: Create a Triangle class that inherits from Shape.
class Triangle(Shape):
# - Initialize it with three vertices, each a tuple of (x, y).
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
# - Implement the measure method to return the area of the triangle using Heron's formula.
    def measure(self):
        length1 = math.sqrt( (self.p2[0] - self.p3[0]) ** 2 + (self.p2[1] - self.p3[1]) ** 2)
        length2 = math.sqrt((self.p1[0] - self.p3[0]) ** 2 + (self.p1[1] - self.p3[1]) ** 2)
        length3 = math.sqrt((self.p2[0] - self.p1[0]) ** 2 + (self.p2[1] - self.p1[1]) ** 2)
        s = (length3 + length2 + length1) / 2
        return math.sqrt(s * (s - length2) * (s - length1) * (s - length3))

if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
