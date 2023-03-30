#!/bin/bash
# A Bash script that takes a URL, sends a request, and displays the body size in bytes.
curl -sI "$1" | grep Content-length | cut -d: -f2 | tr -d " "
