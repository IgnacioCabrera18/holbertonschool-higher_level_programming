#!/usr/bin/python3

"""Define is_kind_of_class(obj, a_class) function"""


def is_kind_of_class(obj, a_class):
    """Return True or Flase"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
