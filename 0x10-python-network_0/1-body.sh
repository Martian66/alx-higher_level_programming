#!/bin/bash
# A bash script that takes in a URL and send a GET request to the URL
curl -sX GET $1 -L
