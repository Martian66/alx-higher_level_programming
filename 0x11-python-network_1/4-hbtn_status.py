#!/usr/bin/python3
# Python script that fetches https://alx-intranet.hbtn.io/status
import requests

response = requests.get('https://alx-intranet.hbtn.io/status')

if response.status_code == 200:
    content = response.json()
    print('Body response:')
    print('\t- type:', type(content))
    print('\t- content:', content)
else:
    print('Error: Request failed with status code', response.status_code)
