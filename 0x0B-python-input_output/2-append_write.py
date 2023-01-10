#!/usr/bin/python3
"""This function appends a string at the end of textfile"""


def append_write(filename="", text=""):
    """Appends string to end of UTF-8 textfile"""

    with open(filename, mode='a', encoding="utf-8") as f:
        new_file = f.write(text)

    return new_file
