#!/usr/bin/python3

"""Define inherits_from(obj, a_class) function"""


def inherits_from(obj, a_class):
    """Return True or Flase"""
    return isinstance(obj, a_class) and type(obj) is not a_class
