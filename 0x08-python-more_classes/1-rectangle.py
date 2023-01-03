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
            """The width of the Rectangle which is an integer value bigger than 0

            Raises:
            TyperError: When the value passed to the setter is not an integer.
            ValueError: When the value passed to the setter is less than or
                        equal to zero.
            """
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            if value < 0:
                raise valueError('width must be >=0')
            self.__width = value

        @property
        def height(self):
            """The height of the Rectangle which is an integer value bigger than 0
            Raises:
            Raises:
            TypeError:  When the value passed to the setter isn't an integer.
            ValueError: When the value passed to the setter is less than or
                        equal to zero.
            """
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError('height must be an integer')
            if value < 0:
                raise ValueError('height must be >= 0')
            self.__height = value
        
