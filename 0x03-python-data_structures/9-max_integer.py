#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_int = my_list[0]
    for index in my_list:
        if index > max_int:
            max_int = index
    return (max_int)
