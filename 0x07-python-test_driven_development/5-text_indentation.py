#!/usr/bin/python3
"""
    This module contains only one function

    The function is described below
"""


def text_indentation(text):
    """
        This function prints a double-spaced formatted text

        Text must be a string which is broken
        after the special characters '?', '.', and ':'
    """

    delims = ['?', ':', '.']

    if type(text) is not str:
        raise TypeError("text must be a string")

    if len(text) == 0:
        print("")

    else:
        text = text.strip()
        new_text = ""
        idx = 0
        while idx < len(text):
            new_text += text[idx]
            if text[idx] in delims:
                new_text += "\n\n"
                idx += 1
            idx += 1
        print(new_text, end="")
