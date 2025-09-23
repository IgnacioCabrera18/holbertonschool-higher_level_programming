#!/usr/bin/python3

"""Define inherits_from(obj, a_class) function"""


def inherits_from(obj, a_class):
    """Return True or Flase"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        False
