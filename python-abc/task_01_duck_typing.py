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
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
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
        ("Circle with radius 0", lambda: Circle(0)),
        ("Circle with negative radius", lambda: Circle(-2)),
        ("Rectangle with width 0", lambda: Rectangle(0, 5)),
        ("Rectangle with negative height", lambda: Rectangle(3, -4)),
        ("Valid Circle", lambda: Circle(2)),
        ("Valid Rectangle", lambda: Rectangle(4, 5))
    ]

    for description, constructor in test_cases:
        print(f"\nTesting: {description}")
        try:
            shape = constructor()
            shape_info(shape)
        except ValueError as e:
            print(e)
