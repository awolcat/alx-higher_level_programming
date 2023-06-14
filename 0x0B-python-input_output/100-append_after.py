#!/usr/bin/python3
"""This module defines a function
"""


def append_after(filename="", search_string="", new_string=""):
    """This function searches for 'search_string' in 'filename'
        and appends the next line after 'search_string'
        with 'new_string'
    """
    new_file = ""
    with open(filename, "r", encoding='utf-8') as search_file:
        for line in search_file:
            new_file += line
            if search_string in line:
                new_file += new_string
    with open(filename, "w", encoding='utf-8') as search_file:
        search_file.write(new_file)
