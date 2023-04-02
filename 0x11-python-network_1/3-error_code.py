#!/usr/bin/python3
# script that takes in a URL and then decodes in utf-8
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
