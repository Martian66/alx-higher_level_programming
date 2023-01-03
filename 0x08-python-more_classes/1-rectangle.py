#!/usr/bin/python3


class Rectangle:
    """A simple Rectangle class being defined.
    """

    def__init__(self, width=0, height=0):
        """Rectangle being initialized with dimensions
        """

        self.height = height
        self.width = width

        @property
        def width(self):
            """ getter for width property """
            return self.__width

        @width.setter
        def width(self, value):
            """ setter for width property """
            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            elif value < 0:
                raise valueError('width must be >=0')
            else:
            self.__width = value

        @property
        def height(self):
            """ getter for height property """
            return self.__height

        @height.setter
        def height(self, value):
            """ setter for height property """
            if not isinstance(value, int):
                raise TypeError('height must be an integer')
            elif value < 0:
                raise ValueError('height must be >= 0')
            else:
                self.__height = value
