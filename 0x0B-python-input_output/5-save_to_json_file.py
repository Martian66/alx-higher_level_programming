#!/usr/bin/python3
"""A function that writes an object to a textfile using JSON"""

import json
# built in python module


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON"""

    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
