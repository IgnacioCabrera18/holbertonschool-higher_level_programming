#!/usr/bin/python3

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """"""
    def __init__(self, radius):
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """"""
    def __init__(self, width, height):
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Width must be a positive number.")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Height must be a positive number.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape_object):
    print(f"Area: {shape_object.area()}")
    print(f"Perimeter: {shape_object.perimeter()}")
