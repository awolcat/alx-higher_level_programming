#!/usr/bin/python3
"""This module defines a script that attempts
    to fetch a url provided and manages any
    HTTPerror
"""
import sys
import urllib.request

if __name__ == '__main___':
    try:
        with urllib.request.urlopen(sys.argv[1]) as req:
            pass
    except Exception as e:
        print('Error code: ', e.code)
