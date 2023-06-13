#!/usr/bin/python3
"""
    This module defines a script that will read input
    from the command line, and store it as a serialized list
    in a JSON file.
    Each new entry from the commandline will be appended to
    the list in the file so that there is only ever 1 list
    at most in the file
"""
from sys import argv
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from__json_file = __import__('6-load_from_json_file').load_from_json_file

# Store arguments in a list
args = []
current = []
args += argv[1: len(argv) + 1]

# Check the contents of our JSON file
filename = "add_item.json"
try:
    with open(filename, "r+", encoding="utf-8") as my_file:
        current = json.load(my_file)
except FileNotFoundError:
    pass

# If contents differ from our list, append our list to current
if current != args:
    current += args

# Then write the new list to our file
with open(filename, "w", encoding="utf-8") as my_file:
    json.dump(current, my_file)
