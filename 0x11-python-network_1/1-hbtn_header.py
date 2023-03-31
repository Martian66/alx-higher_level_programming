#!/usr/bin/python3
# A Python script that gets the X-Request-Id value from a URL response header
import urllib.request
import sys

if __name__ == "__main__":
    """
    gets the X-Request-Id value from a url response header
    """
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        req_id = response.info().get('X-Request-Id')
        print(req_id)
