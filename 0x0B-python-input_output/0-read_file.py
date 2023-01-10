#!/usr/bin/python3
"""A function that reads a textfile and prints it to stdout"""


def read_file(filename=""):
    """Prints a textfile(UTF-8) to stdout"""
    with open(filename, "r", enconding="utf-8") as f:
        print(f.read(), end="")
