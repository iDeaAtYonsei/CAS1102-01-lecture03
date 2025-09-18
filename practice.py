from abc import *
import math
from typing import List


class Shape(ABC):
    @abstractmethod
    def measure():
        raise NotImplementedError("Subclasses must implement this method.")

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
    
    def measure(self):
        return math.pi * self.__radius * self.__radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__length = height
    
    def measure(self):
        return self.__width*self.__length
    
class Triangle():
    def __init__(self, p1, p2, p3):
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3

    def findLength(self, v1, v2):
        return math.sqrt((v2[0] - v1[0])**2 + (v2[1] - v1[1])**2)
        
    def measure(self):
        a = self.findLength(self.__p1, self.__p2)
        b = self.findLength(self.__p1, self.__p3)
        c = self.findLength(self.__p2, self.__p3)
        s = (a+b+c)/2
        print(math.sqrt(s * (s-a) * (s-b) * (s-c)))
        return math.sqrt(s*(s-a)*(s-b)*(s-c))
    
if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
