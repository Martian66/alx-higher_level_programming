#!/usr/bin/python3
# sends a POST request to http://0.0.0.0:5000/search_user
import requests
import sys

if __name__ == "__main__":
    val = "" if len(sys.argv) == 1 else sys.argv[1]
    response = requests.post("http://0.0.0.0:5000/search_user", {"q": val})

    try:
        data = response.json()
        if not data:
            print("No result")
        else:
            print("[{}] {}".format(data["id"], response.get["name"]))
    except ValueError:
        print("Not a valid JSON")
