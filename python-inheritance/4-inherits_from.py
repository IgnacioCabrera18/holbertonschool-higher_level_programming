#!/usr/bin/python3

"""Define inherits_from(obj, a_class) function"""


def inherits_from(obj, a_class):
    """Return True or Flase"""
    if not type(obj) is a_class:
        return True
    else:
        False
