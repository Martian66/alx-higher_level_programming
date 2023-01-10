#!/usr/bin/python3
"""A function that reads a textfile and prints it to stdout"""


def read_file(filename=""):
    """File opened in text mode allowing for accessibility"""
    with open(filename, enconding="utf=8") as f:
        for line in f:
            print(line, end="")
