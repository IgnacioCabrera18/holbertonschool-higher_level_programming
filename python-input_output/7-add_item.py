#!/usr/bin/env python3

"""Module add_items_to_json_file"""
import sys
from os import path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def add_items_to_json_file(filename):
    """Function add itemsto json file"""
    my_list = load_from_json_file(filename)
    arguments_to_add = sys.argv[1:]
    my_list.extend(arguments_to_add)
    save_to_json_file(my_list, filename)

if __name__ == "__main__":
    json_filename = "add_item.json"
    add_items_to_json_file(json_filename)
