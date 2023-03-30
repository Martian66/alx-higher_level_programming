#!/usr/bin/python3
# A function that finds a peak in a list of unsorted integers.
def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted ints
    Args:
    list_of_integers (list): A list of unsorted ints
    Returns:
    int: The peak element in the list.
    """
    Complexity:
        O(log(n))
    left, right = 0 len(list_of_integers) - 1
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]
