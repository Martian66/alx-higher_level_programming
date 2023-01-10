#!/usr/bin/python3
"""This is a Python class-to-JSON function"""


def class_to_json(obj):
    """Returns a dictionary representation of a simple data structure"""
    return vars(obj)
