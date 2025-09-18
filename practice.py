from typing import List
from math import pi, sqrt

class Shape:
    # TODO: Define the method "measure".
    """
    - This is an abstract method, so it should just raise NotImplementedError.
    """
    def measure(self):
        raise NotImplementedError


class Circle(Shape):
    # - Initialize it with a radius (float).
    # - Implement the measure method to return the area of the circle.
    def __init__(self, radius):
        self.radius=float(radius)
    def measure(self):
        return pi*self.radius*self.radius


class Rectangle(Shape):
    # - Initialize it with width and height (floats).
    # - Implement the measure method to return the area of the rectangle.
    def __init__(self, width, height):
        self.width=width
        self.height=height

    def measure(self):
        return self.width*self.height



class Triangle(Shape):
    # - Initialize it with three vertices, each a tuple of (x, y).
    # - Implement the measure method to return the area of the triangle using Heron's formula.
    def __init__(self, p1, p2, p3):
        self.p1=p1
        self.p2=p2
        self.p3=p3
    def measure(self):
        x1, y1=self.p1
        x2, y2=self.p2
        x3, y3=self.p3
        a=sqrt((x2-x1)**2+(y2-y1)**2)
        b=sqrt((x3-x2)**2+(y3-y2)**2)
        c=sqrt((x3-x1)**2+(y3-y1)**2)
        s=(a+b+c)/2

        return sqrt(s*(s-a)*(s-b)*(s-c))


if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
