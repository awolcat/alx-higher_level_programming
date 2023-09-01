#!/usr/bin/python3
"""This module defines a script that will
    list 10 commits (from the most recent to oldest)
    of the repository “rails” by the user “rails”
"""
import sys
import requests

if __name__ == '__main__':
    owner = sys.argv[1]
    repo = sys.argv[2]

    URL = f'https://api.github.com/repos/{owner}/{repo}/commits'

    response = requests.get(URL)

    for index in range(0, 10):
        commit = response.json()[index]
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print('{}: {}'.format(sha, author))
