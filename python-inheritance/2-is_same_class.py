#!/usr/bin/python3

"""Define is_same_class(obj, a_class) function"""


def is_same_class(obj, a_class):
    """Return TRue or False"""
    if type(obj) is a_class:
        return True
    else:
        return False
