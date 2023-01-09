#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """This class represents a base geometry"""
    def area(self):
        """Instance method not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Determines if a value is an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

        class Rectangle(BaseGeometry):
            def __init__(self, width, height):
                self.integer_validator("width", width)
                self.integer_validator("height", height)
                self.__width = width
                self.__height = height
