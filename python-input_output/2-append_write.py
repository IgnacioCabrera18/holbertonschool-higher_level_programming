#!/usr/bin/python3

"""Module appedn_write"""


def append_write(filename="", text=""):
    """Function append_write"""
    with open(filename, 'a', encoding="utf-8") as f:
        num_append = f.write(text)
    return num_append
