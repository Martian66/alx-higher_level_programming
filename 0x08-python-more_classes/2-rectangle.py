#!/usr/bin/python3
"""A class that defines a rectangle"""

class Rectangle:
    """this represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Intializing this rectangle class
        Args:
        width: represents the width of the tectangle
        height: represents the height of the rectangle
        Raises:
            TypeError: if the size is not integer
            ValueError: if the size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value