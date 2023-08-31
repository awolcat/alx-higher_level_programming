#!/bin/bash
# sends a GET request to URL, and displays the body of the response
curl -sL "$1" | awk 'NR==1{body=1} body; /^200$/ && body'
