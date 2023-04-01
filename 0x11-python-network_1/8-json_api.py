#!/usr/bin/python3
# sends a POST request to http://0.0.0.0:5000/search_user
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    response = requests.post(url, data={"q": q})
    try:
        data = response.json()
        if 'id' in data and 'name' in data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            if not data:
                print("No result")
            else:
                print("Unexpected response: {}".format(data))
