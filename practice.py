from typing import List
import math

class Shape(List):
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
    def __init__(self,radius):
        self.r=radius
        
    def measure(self):
        return self.r**2*math.pi

# TODO: Create a Rectangle class that inherits from Shape.
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.
class Rectangle(Shape):
    def __init__(self,width,height):
        self.w = width
        self.h = height
        
    def measure(self):
        return self.w*self.h

# TODO: Create a Triangle class that inherits from Shape.
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.
class Triangle(Shape):
    def __init__(self,p1,p2,p3):
        self.p1=p1
        self.p2=p2
        self.p3=p3
    def measure(self):
        a = math.sqrt((self.p1[1]-self.p2[1])**2+(self.p1[0]-self.p2[0])**2)
        b = math.sqrt((self.p2[1]-self.p3[1])**2+(self.p2[0]-self.p3[0])**2)
        c = math.sqrt((self.p1[1]-self.p3[1])**2+(self.p1[0]-self.p3[0])**2)
        s = (a+b+c)/2
        return math.sqrt(s*(s-a)*(s-b)*(s-c))

if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
