#!/usr/bin/python3
# script that takes in a URL and then decodes in utf-8

import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            print(response.read().decode("ascii"))
    except urllib.error. HTTPError as e:
        print("Error code: {}".format(e.code))
