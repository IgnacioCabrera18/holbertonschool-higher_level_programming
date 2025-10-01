#!/usr/bin/python3

"""Module add_items_to_json_file"""
import os.path
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':

    filename = "add_item.json"

    if os.path.exists("./add_item.json"):
        my_list = list(load_from_json_file(filename))
    else:
        my_list = []

    for arg in sys.argv[1:]:
        my_list.append(arg)

    save_to_json_file(my_list, filename)
