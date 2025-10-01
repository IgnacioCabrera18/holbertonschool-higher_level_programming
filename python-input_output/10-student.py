#!/usr/bin/python3

"""Define a class Student"""


class Student:
    """Represente a Student"""
    def __init__(self, first_name, last_name, age):
        """Initalize a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
