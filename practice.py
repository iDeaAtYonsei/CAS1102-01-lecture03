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
        self.r=radius

    def measure(self):
        return math.pi*self.r*self.r

# TODO: Create a Rectangle class that inherits from Shape.
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.
class Rectangle(Shape):
    def __init__(self, width, height):
        self.w=width
        self.h=height

    def measure(self):
        return self.w*self.h

# TODO: Create a Triangle class that inherits from Shape.
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.
class Triangle(Shape):
    def __init__(self, p1, p2, p3):
        self.l1=((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**1/2
        self.l2=((p2[0]-p3[0])**2+(p2[1]-p3[1])**2)**1/2
        self.l3=((p3[0]-p1[0])**2+(p3[1]-p1[1])**2)**1/2
        self.s=(self.l1+self.l2+self.l3)/2

    def measure(self):
        return (self.s*(self.s-self.l1)*(self.s-self.l2)*(self.s-self.l3))**(1/2)

if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
