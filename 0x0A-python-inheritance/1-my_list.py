#!/usr/bin/python3
"""
module for my lists
"""


class Mylist(list):
    """
    returns my list in assorted order
    """

    def print_sort(self):
        """
        sorts values in ascending order
        """
        print(sorted(self))
