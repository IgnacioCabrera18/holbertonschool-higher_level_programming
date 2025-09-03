#!/usr/bin/python3
def uppercase(str):
    result_str = ""
    for a in str:
        if 'a' <= a <= 'z':
            result_str = result_str + chr(ord(a) - 32)
        else:
            result_str = result_str + a
    print("{}".format(result_str))
