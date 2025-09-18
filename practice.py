from typing import List


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
        self.__radius = float(radius)  # private variable
    
    def measure(self):
        return math.pi * (self.__radius ** 2)



# TODO: Create a Rectangle class that inherits from Shape.
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.
# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = float(width)
        self.__height = float(height)
    
    def measure(self):
        return self.__width * self.__height


# TODO: Create a Triangle class that inherits from Shape.
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
    def measure(self):
        s = (self.__a + self.__b + self.__c) / 2  # semi-perimeter
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))


if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
