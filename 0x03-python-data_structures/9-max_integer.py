#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    max_integer = 0
    for index in my_list:
        if index > max_integer:
            max_integer = index
    return max_integer
