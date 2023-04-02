#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials
and uses the GitHub API to display your id
"""
import requests
import sys

username = sys.argv[1]
password = sys.argv[2]

url = 'https://api.github.com/user'

response = requests.get(url, auth=(Martian66, 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))

if response.status_code == 200:
    data = response.json()
    user_id = data['id']
    print(f"Your user ID is {user_id}")
else:
print("Failed to retrieve user ID. Please check your credentials and try again.")
