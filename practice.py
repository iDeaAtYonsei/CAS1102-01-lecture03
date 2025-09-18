import math
from typing import List


class Shape:
    # TODO: Define the method "measure".
    """
    - This is an abstract method, so it should just raise NotImplementedError.
    """
    def measure(self):
        raise NotImplementedError


# TODO: Create a Circle class that inherits from Shape.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = float(radius)
    def measure(self):
        return math.pi*(self.radius**2)
# - Initialize it with a radius (float).
# - Implement the measure method to return the area of the circle.


# TODO: Create a Rectangle class that inherits from Shape.
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width= float(width)
        self.height=float(height)
    def measure(self):
        return self.width*self.height

# TODO: Create a Triangle class that inherits from Shape.
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.
class Triangle(Shape):
    def __init__(self,p1,p2,p3):
        self.p1 = tuple(p1)
        self.p2 = tuple(p2)
        self.p3 = tuple(p3)
    def distance(self,a,b):
        return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    def measure(self):
        a=self.distance (self.p1,self.p2)
        b=self.distance (self.p2,self.p3)
        c=self.distance (self.p1,self.p3)
        s=(a+b+c)/2
        return math.sqrt(s*(s-a)*(s-b)*(s-c))
if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
