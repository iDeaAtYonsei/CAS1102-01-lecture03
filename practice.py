from typing import List


class Shape:
    # TODO: Define the method "measure".
    """
    - This is an abstract method, so it should just raise NotImplementedError.
    """


class Circle(Shape):
    # TODO: Implement the constructor
    """
    - Initialize a Circle with one parameter: radius.
    - Store radius as float for consistent calculations.
    """

    # TODO: Implement "measure" to return the area of the circle.


class Rectangle(Shape):
    """
    - Initialize a Rectangle with two parameters: width and height.
    - Store them as float for consistent calculations.
    """

    # TODO: Implement "measure" to return the area of the rectangle.


class Triangle(Shape):
    """
    - Initialize a Triangle with three vertex coordinates (p1, p2, p3).
    - Each vertex should be a tuple of (x, y).
    """

    # TODO: Implement "measure" to return the area of the triangle.
    """
    - Use Heron's formula.
    """


if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
