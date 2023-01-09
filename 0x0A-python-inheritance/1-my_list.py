#!/usr/bin/python3
"""
Module for my lists
"""


class Mylist(list):
    """Returns my list in assorted order"""
    def print_sort(self):
        """Sorts values in ascending order"""
        print(sorted(self))
