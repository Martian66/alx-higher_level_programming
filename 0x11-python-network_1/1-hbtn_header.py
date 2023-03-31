#!/usr/bin/python3
# A Python script that gets the X-Request-Id value from a URL response header
import urllib.request
from sys import argv

if __name__ == "__main__":
    """
    gets the X-Request-Id value from a url response header
    """
    with urllib.request.urlopen(argv[1]) as response:
        req_id = response.info().get('X-Request-Id')
        print(req_id)
