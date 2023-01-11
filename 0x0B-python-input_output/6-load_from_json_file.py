#!/usr/bin/python3
"""A function that creates an object from a "JSON file" """

import json
# built in python module


def load_from_json_file(filename):
    """Creates an object from a "JSON file" """

    with open(filename, "r") as f:
        return json.load(f)
