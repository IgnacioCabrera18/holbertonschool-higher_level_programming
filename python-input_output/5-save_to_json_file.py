#!/usr/bin/python3

"""Module save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Function to return json.dump"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
