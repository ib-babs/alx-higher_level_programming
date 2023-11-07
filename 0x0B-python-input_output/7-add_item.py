#!/usr/bin/python3
"""
Function module
"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_item():
    """add_item function"""
    arg_list = [i for i in sys.argv[1:]]

    save_to_json_file(arg_list, "add_item.json")
    load_from_json_file("add_item.json")


add_item()
