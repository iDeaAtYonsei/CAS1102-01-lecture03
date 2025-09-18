from typing import List
import math

class Shape:
    # TODO: Define the method "measure".
    def measure(self):
        raise NotImplementedError("This method should be implemented by subclasses.")
    """
    - This is an abstract method, so it should just raise NotImplementedError.
    """


# TODO: Create a Circle class that inherits from Shape.
# - Initialize it with a radius (float).
# - Implement the measure method to return the area of the circle.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def measure(self):
        return math.pi * self.radius ** 2

# TODO: Create a Rectangle class that inherits from Shape.
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def measure(self):
        return self.width * self.height

# TODO: Create a Triangle class that inherits from Shape.
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.
class Triangle(Shape):
    def __init__(self, point1 : tuple, point2 : tuple, point3 : tuple):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
    
    def measure(self):
        length1 = math.sqrt((self.point2[0] - self.point1[0]) ** 2 + (self.point2[1] - self.point1[1]) ** 2)
        length2 = math.sqrt((self.point3[0] - self.point2[0]) ** 2 + (self.point3[1] - self.point2[1]) ** 2)
        length3 = math.sqrt((self.point1[0] - self.point3[0]) ** 2 + (self.point1[1] - self.point3[1]) ** 2)
        s = (length1 + length2 + length3) / 2
        return math.sqrt(s * (s - length1) * (s - length2) * (s - length3))

if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(point1=(0, 0), point2=(3, 0), point3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
