#!/usr/bin/python3
# script that takes in a URL and then decodes in utf-8
from urllib.request
from urllib.error
import sys

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print(body)
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
