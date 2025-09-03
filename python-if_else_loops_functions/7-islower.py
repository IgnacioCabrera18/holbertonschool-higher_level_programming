#!/usr/bin/python3
def islower(c):
    char_ascii = ord(c)
    if char_ascii >= 97 and char_ascii <= 122:
        return True
    else:
        return False
