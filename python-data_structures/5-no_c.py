#!/usr/bin/python3
def no_c(my_string):
    remove_c = ""
    for a in my_string:
        if a == 'c' or a == 'C':
            continue
        else:
            remove_c += a
    return remove_c
