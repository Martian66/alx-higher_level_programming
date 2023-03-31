#!/usr/bin/python3
# Write a Python script that retrieves the X-Request-Id value from a URL response header

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:

    x_request_id = response.getheader('X-Request-Id')
    print(f"The value of the X-Request-Id variable is {x_request_id}")
