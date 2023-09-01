#!/usr/bin/python3
"""Module defines a script that gets the value
    of a specific header var from headers returned by
    the url provided
    Usage: 1-hbtn_header.py <url>
"""
import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as req:
    print(req.headers.get('X-Request-Id'))
