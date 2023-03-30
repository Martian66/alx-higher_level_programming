#!/bin/bash
# A Bash script that takes in a URL, sends a POST request to the passed URL
url="$1"
email="test@gmail.com"
subject="I will always be here for PLD"
curl -sS -X POST -d "email=$email&subject=$subject" "$url"
