#!/bin/bash
# A Bash script that takes a URL, sends a request, and displays the body size in bytes.
read -p "Enter URL: " url

curl -s -o output.txt -w "%{size_download}" $url

size=$(cat output.txt)
echo "Size of the body: $size bytes"

rm output.txt
