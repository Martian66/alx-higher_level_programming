#!/usr/bin/python3
"""Function defining a student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = fist_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        new_dictionary = {}
        for key, value in self.__dict__.item():
            if key in attrs:
                new_dictionary[key] = value
        return new_dictionary
