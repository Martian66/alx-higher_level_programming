#!/usr/bin/python3
""" A function that writes a string to a text file and
returns the number of characters written"""


def write_file(filename="", text=""):
    """File made accessible to write and
    then return the number of characters written"""
    with open(filename, mode='w', encoding="utf-8") as f:
        new_file = f.write(text)

        return new_file
