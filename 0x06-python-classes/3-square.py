#!/usr/bin/python3
class Square:
    """Represents a square."""

    def__init__(self, size=0):
         """Initialize a new Square.

         Args:
            size (int): the size of the new square
            """
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if sizee < 0:
                raise ValueError("size must be >= 0")
            self.__size = size

    def area(self):
        return self.__size**2
