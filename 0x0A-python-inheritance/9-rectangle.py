#!/usr/bin/python3
"""Defines a class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeomtry


class Rectangle(BaseGeometry):
    """This class represents a base geometry"""

    def __init__(self, width, height):
        """Initialize a new Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


def area(self):
    """Returns the area of a rectangle"""
    return self.__height * self.__width


def __str__(self):
    """Returns the printed string value of a Rectangle"""
    return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
