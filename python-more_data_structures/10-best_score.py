#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    value = list(a_dictionary.keys())[0]
    for key in a_dictionary:
        if key > value:
            value = key
    return value
