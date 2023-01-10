#!/usr/bin/python3
"""A function that reads a textfile and prints it to stdout"""


def read_file(filename=""):
    """File opened in text mode allowing for accessibility"""
    f = open('filename', 'r', enconding="utf-8")
    """File being read and then closed upon success"""
    with open('filename', enconding='utf=8') as f:
        read_file = f.read()

        f.closed

        True
