#!/usr/bin/python3
# A Python script that gets the X-Request-Id value from a URL response header

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.info()
    x_request_id = headers.get('X-Request-Id')
    print(x_request_id)
