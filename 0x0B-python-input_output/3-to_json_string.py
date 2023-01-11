#!/usr/bin/python3
"""A function that returns the JSON representation of an object"""

import json
# built in python module
def to_json_string(my_obj):
    """Returns the JSON represention of an object"""
    return json.loads(my_obj)