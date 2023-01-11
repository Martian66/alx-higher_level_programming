#!/usr/bin/python3
"""A function that returns the JSON representation of an object"""

import json
# built in python module
<<<<<<< HEAD
def to_json_string(my_obj):
    """Returns the JSON represention of an object"""
    return json.loads(my_obj)
=======


def to_json_string(my_obj):
    """Returns the JSON represention of an object"""
    return json.dumps(my_obj)
>>>>>>> 9172cd69e2f1a6b3fe30ed7785cd11ab3dc356e3
