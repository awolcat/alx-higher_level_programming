#!/usr/bin/python3
"""This module defines a script that attempts
    to fetch a url provided and manages any
    HTTPerror
"""
import sys
import urllib.request

try:
    req = urllib.request.urlopen(sys.argv[1])
except Exception as e:
    print('Error code: ', e.code)
