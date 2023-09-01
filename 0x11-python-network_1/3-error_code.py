#!/usr/bin/python3
"""This module defines a script that attempts
    to fetch a url provided and manages any
    HTTPerror
"""
import sys
import urllib.request
from urllib.error import URLError
if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as req:
            response = req.read()
            print(response.decode('utf-8'))
    except URLError as e:
        print('Error code: ', e.status)
