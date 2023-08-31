#!/usr/bin/bash
# Get the size of the response body of a http request
curl -sI "$1" | grep 'Content-Length' | sed "s/[^0-9]//g"
