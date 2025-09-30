#!/usr/bin/python3

"""Module read_file."""


def read_file(filename=""):
    """Function read a file"""
    with open(filename, "r", encoding='UTF8') as f:
        print(f.read())
