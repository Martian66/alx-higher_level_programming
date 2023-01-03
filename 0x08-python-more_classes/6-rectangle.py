#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """
    This class has two attributes
    width
    height
    both will have property and setter function definition
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        instantiates width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
	"""Returns the area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """Returns perimeter of a rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return ((self.width + self.height) * 2)

    def __str__(self):
	 """presents a diagram of the rectangle defined for an object"""
        if self.width == 0 or self.height == 0:
            return ("")
        width = "#" * self.width
        rectangle = width
        for x in range(self.height - 1):
            rectangle += "\n" + width
        return (rectangle)

    def __repr__(self):
	"""returns a string representation of the rectangle"""
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
	"""prints a message for every object that is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
