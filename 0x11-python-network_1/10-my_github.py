#!/usr/bin/python3
"""This module defines a script that takes your 
    GitHub credentials (username and password) 
    and uses the GitHub API to display your id
"""
import sys
import requests

if __name__ == '__main__':
    user = sys.argv[1]
    passw = sys.argv[2]
    URL = 'https://api.github.com/user'
    response = requests.get(URL, auth=(user, passw))
    print(response.json().get('id'))
