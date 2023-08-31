#!/bin/bash
# Print only the response code
curl -sLw "%{http_code}" "$1"
