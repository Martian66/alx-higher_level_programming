#!/usr/bin/python3
"""Checks if object is an instance of a class
or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """Returns true if object is an instance of a class
    or an inherited class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
