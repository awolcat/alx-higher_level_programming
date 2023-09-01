#!/usr/bin/python3
"""This module defines a script to fetch the page
    at https://alx-intranet.hbtn.io/status
"""
import urllib.request
URL = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(URL) as req:
    response = req.read()
    print("Body response:")
    print(f"\t- type: {type(response)}")
    print(f"\t- content: {response}")
    print(f"\t- utf8 content: {response.decode()}")
