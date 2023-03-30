#!/bin/bash
# A Bash script that takes a URL, sends a request, and displays the body size in bytes.
curl -sL "$1" | wc -c
