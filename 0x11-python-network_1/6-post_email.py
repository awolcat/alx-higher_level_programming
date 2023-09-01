#!/usr/bin/python3
"""This module defines a script that uses requests package
    to apply the HTTP POST method and prints the response body
"""
import sys
import requests

if __name__ == '__main__':
    payload = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], data=payload)
    print(response.text)
