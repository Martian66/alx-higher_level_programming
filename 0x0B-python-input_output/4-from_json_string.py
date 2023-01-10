#!/usr/bin/python3
"""A function that returns a python object using JSON"""


import json
# built in python module


def from_json_string(my_str):
    """Returns a python object using JSON"""
    return json.loads(my_str)
