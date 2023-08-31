#!/bin/bash
# sends a DELETE request to the URL passed and displays the body of the response
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
