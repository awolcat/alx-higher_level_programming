#!/usr/bin/python3
"""This module defines a script that attempts
    to fetch a url provided and manages any
    HTTPerror
"""
import sys
import urllib.request
from urllib.error import HTTPError
if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as req:
            print(req.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: ', e.code)
