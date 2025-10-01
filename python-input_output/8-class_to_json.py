#!/usr/bin/python3

"""Module class_to_json"""


def class_to_json(obj):
    """Function return json_dict"""
    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
