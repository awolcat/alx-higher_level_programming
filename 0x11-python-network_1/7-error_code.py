#!/usr/bin/python3
"""This module defines a script that attempts to fetch
    a URL and prints the response body or the error code
    if a http or server error (>=400)
    Usage: 7-error_code.py <url>
"""
import sys
import requests

if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    if response.status_code < 400:
        print('{}'.format(response.text))
    else:
        print('Error code: {}'.format(response.status_code))
