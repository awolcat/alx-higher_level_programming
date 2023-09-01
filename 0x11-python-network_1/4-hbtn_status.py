#!/usr/bin/python3
"""This module defines a script that fetches
    https://alx-intranet.hbtn.io/status
    using the requests package
"""
import requests
if __name__ == '__main__':
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print(f'\t- type: {type(response.text)}')
    print(f'\t- content: {response.text}')
