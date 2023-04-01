#!/usr/bin/python3
# sends a POST request to the passed URL with the email as a parameter
import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

print("Your email is:", email)

response = requests.post(url, data={'email': email})

print(response.text)
