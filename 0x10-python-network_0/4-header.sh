#!/bin/bash
# This Bash script takes in a URL as an argument, sends a GET request to the URL
curl -sS -H "X-School-User-Id: 98" "$1"
