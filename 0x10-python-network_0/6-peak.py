#!/usr/bin/python3
# A function that finds a peak in a list of unsorted integers.
def find_peak(lst):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        lst (list): A list of unsorted integers.

    Returns:
        int: The peak element in the list.
    """
    length = len(lst)
    if length == 0:
        return None
    if length == 1:
        return (lst[0])
    if length == 2:
        return lst[0] if lst[0] >= lst[1] else lst[1]

    for idx in range(0, length):
        value = lst[idx]
        if (idx > 0 and idx < length - 1 and
                lst[idx + 1] <= value and lst[idx - 1] <= value):
            return value
        elif idx == 0 and lst[idx + 1] <= value:
            return value
        elif idx == length - 1 and lst[idx - 1] <= value:
            return value
    return pick
