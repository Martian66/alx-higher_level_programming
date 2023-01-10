#!/usr/bin/python3
"""A function that reads a textfile and prints it to stdout"""


def read_file(filename=""):
    """Prints a UTF-8 text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
