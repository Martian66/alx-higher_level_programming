#!/usr/bin/python3
"""Defines a class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A class to define a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
