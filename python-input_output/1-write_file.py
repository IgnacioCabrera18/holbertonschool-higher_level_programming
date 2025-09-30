#!/usr/bin/python3

""""""


def write_file(filename="", text=""):
    """"""
    with open(filename, 'w', encoding="utf-8") as f:
        num_write = f.write(text)
    return num_write
