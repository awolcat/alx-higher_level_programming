#!/usr/bin/python3
"""This module defines a script that sends a post
    request with requests library with the data
    provided
"""
import sys
import requests
if __name__ == '__main__':
    URL = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) >= 2 and sys.argv[1].isalpha():
        payload = {'q': sys.argv[1]}
    else:
        payload = {'q': ""}

    try:
        response = requests.post(URL, data=payload)
        json = response.json()
        if len(json) < 1:
            print('No result')
        else:
            id = json.get('id')
            name = json.get('name')
            print(f'[{id}] {name}')
    except requests.ecxeptions.JSONDecodeError as e:
        print('Not a valid JSON')
