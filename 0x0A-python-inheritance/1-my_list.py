#!/usr/bin/python3
"""Module for my list."""


class MyList(list):
    """A class that inherits from list"""
    def print_sort(self):
        """prints a sorted list"""
        print(sorted(self))
