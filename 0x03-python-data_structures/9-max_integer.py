#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    max_int = my_list[0]
    for index in my_list[0]:
        if index > max_int:
            max_int = index
    return (max_int)
