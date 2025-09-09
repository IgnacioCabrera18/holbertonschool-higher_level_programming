#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_value = list(a_dictionary.keys())[0]
    compare = a_dictionary[max_value]
    for key, value in a_dictionary.items():
        if value > compare:
            compare = value
            max_value = key
    return max_value
