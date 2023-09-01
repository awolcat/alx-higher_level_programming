#!/usr/bin/python3
"""This module defines a script that attempts to fetch
    a URL and prints the response body or the error code
    if a http or server error (>=400)
    Usage: 7-error_code.py <url>
"""
import sys
import requests

if __name__ == '__main__':
    try:
        response = requests.get(sys.argv[1])
        err = response.raise_for_status()
        print('{}'.format(response.text))
    except Exception:
        if response.status_code >= 400:
            print('Error code: {}'.format(response.status_code))
