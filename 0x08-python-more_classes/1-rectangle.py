#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """
    Rectangle functions and data
    """

    def __init__(self, width=0, height=0):
        """Instantiation
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets width attributes"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width attributes"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
