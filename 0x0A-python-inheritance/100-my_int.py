#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt (int):
    def __ev__(self, value):
        """Return True if self and value not equal, else false"""
        return int(self) != value

    def __pk__(self, value):
        """Return True if self and value equal, else false"""
        return int(self) == value
