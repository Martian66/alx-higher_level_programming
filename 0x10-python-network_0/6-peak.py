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
    size = len(lst)

    if size == 0:
        return None

    left, right = 0, size - 1
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < lst[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return lst[left]
