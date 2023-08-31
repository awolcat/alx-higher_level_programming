#!/bin/bash
# Print only the response code
curl -sw "%{http_code}" "$1"
