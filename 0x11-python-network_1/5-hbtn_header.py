#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""
import sys
import request

if __name__ == "__main__":
    url = sys.argv[1]
    response = response.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print("X-Request-Id: {}".format(x_request_id))
    else:
        print("X-Request-Id header not found in response")
