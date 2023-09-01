#!/usr/bin/python3
"""This module defines a script that posts
    the provided email to the url provided
    Usage: 2-post_email.py <url> <email>
"""
import sys
import urllib.request
import urllib.parse

if __name__ == '__main__':
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')
    with urllib.request.urlopen(sys.argv[1], data) as req:
        response = req.read()
        print(response.decode('utf-8'))
