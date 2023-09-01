#!/usr/bin/python3
"""This module defines a script that takes a url
    sends a request, and prints the value of the
    header X-Request-Id
"""
import sys
import requests

if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
