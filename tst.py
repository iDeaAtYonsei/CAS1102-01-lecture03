from typing import List


class Shape:
    # TODO: Define the method "measure".
    def measure(self):
        raise NotImplementedError
    """
    - This is an abstract method, so it should just raise NotImplementedError.
    """


# TODO: Create a Circle class that inherits from Shape.
# - Initialize it with a radius (float).
# - Implement the measure method to return the area of the circle.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = float(radius)
    def measure(self, radius):
        area = radius **2
        return area

# TODO: Create a Rectangle class that inherits from Shape.
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)
    def measure(self, width, height):
        area = width * height
        return area


# TODO: Create a Triangle class that inherits from Shape.
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.

class Triangle(Shape):

    def measure(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        a = ((float(p1[0]) - float(p2[0])) ** 2 + (float(p1[1]) - float(p2[1])) ** 2) ** 0.5
        b = ((float(p2[0]) - float(p3[0])) ** 2 + float((p2[1]) - float(p3[1])) ** 2) ** 0.5
        c = ((float(p3[0]) - float(p1[0])) ** 2 + (float(p3[1]) - float(p1[1])) ** 2) ** 0.5

        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ^ (1 / 2)
        return area


if __name__ == "__main__":
    shapes: List[Shape] = [
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])