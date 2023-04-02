#!/usr/bin/python3
"""
 A Python script that gets the X-Request-Id value from a URL response header
 using the packages urllib and sys
 """
import urllib.request
from sys import argv


if __name__ == "__main__":
    """
    gets the X-Request-Id value from a url response header
    """
    url = argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
