#!/usr/bin/python3

"""Define a class Mylist"""


class MyList(list):
    """Reprecente Mylist inherits from list"""
    def print_sorted(self):
        print(sorted(self))
