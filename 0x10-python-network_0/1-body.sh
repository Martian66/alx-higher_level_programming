#!/bin/bash
# A bash script that takes in a URL and send a GET request to the URL
curl -s "$1" | { read status; [ "$status" = "HTTP/1.1 200 OK" ] && cat || echo "Error: Response status code is ${status##* }"; }
