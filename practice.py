from typing import List
class Shape:
    def measure(self):
        raise NotImplementedError

    # TODO: Define the method "measure".
    """
    - This is an abstract method, so it should just raise NotImplementedError.
    """



# TODO: Create a Circle class that inherits from Shape.
# - Initialize it with a radius (float).
# - Implement the measure method to return the area of the circle.
class Circle(Shape):
    def __init__(self, radius):
        self.r = r

    def measure(self):
        return math.pi * (self.ridius ** 2)

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

import math

class Triangle(Shape):
    def __init__(self, p1, p2, p3):
        """
        p1, p2, p3: 각각 (x, y) 형태의 튜플
        예: (0, 0), (3, 0), (0, 4)
        """
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def measure(self):
        # 각 변의 길이 계산
        a = math.dist(self.p1, self.p2)
        b = math.dist(self.p2, self.p3)
        c = math.dist(self.p3, self.p1)

        # 반둘레 (semi-perimeter)
        s = (a + b + c) / 2

        # Heron's formula
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area


# 실행 예시
if __name__ == "__main__":
    t = Triangle((0, 0), (3, 0), (0, 4))
    print("Triangle area:", t.measure())  # 6.0 출력



if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
