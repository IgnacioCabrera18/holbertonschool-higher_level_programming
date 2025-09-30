#!/usr/bin/python3

"""Module write_file"""


def write_file(filename="", text=""):
    """Function write a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        num_write = f.write(text)
    return num_write
