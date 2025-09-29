#!/usr/bin/python3

import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number.")
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        if not isinstance(width, (int, float)):
            raise TypeError("Width must be a number.")
        if not isinstance(height, (int, float)):
            raise TypeError("Height must be a number.")
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

if __name__ == "__main__":
    test_cases = [
        ("Circle radius 0", lambda: Circle(0)),
        ("Circle negative radius", lambda: Circle(-5)),
        ("Rectangle width 0", lambda: Rectangle(0, 5)),
        ("Rectangle negative height", lambda: Rectangle(3, -4)),
        ("Valid Circle", lambda: Circle(5)),
        ("Valid Rectangle", lambda: Rectangle(3, 4)),
    ]

    for description, func in test_cases:
        print(f"\nTesting: {description}")
        try:
            shape = func()
            shape_info(shape)
        except (ValueError, TypeError) as e:
            print(e)
