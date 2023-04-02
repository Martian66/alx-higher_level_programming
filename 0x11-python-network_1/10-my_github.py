#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials
and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(user_name, password))
    try:
        print(response.json()["id"])
    except KeyError:
        print("None")
