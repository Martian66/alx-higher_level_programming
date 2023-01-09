#!/usr/bin/python3
"""checks if object is an instance of a class
inherited from the class or not"""


def inherits_from(obj, a_class):
    """Returns true if object is an instance of a class inherited,
    directly or indirectly from the specified class, else False
    """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return False
