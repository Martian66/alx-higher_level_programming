#!/bin/bash
# A bash script that takes in a URL and send a GET request to the URL
curl -s -w '%{http_code}' "$1" | { read status; [ "$status" = "200" ] && curl -s "$1" echo "Error: Response status code is $status"; } | tail -n +2
