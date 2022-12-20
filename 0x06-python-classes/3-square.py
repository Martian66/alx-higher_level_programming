#!/usr/bin/python3
"""define a class square"""


class Square:
    """Represents a square."""

    def__init__(self, size=0):
         """Initialize a new Square.

         Args:
            size (int): the size of the new square
            """
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
