#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_integers):
    """
    Args:
        list_integers(int): list of integers to find peak 
    Returns: peak of list_integers
    """
    size = len(list_integers)
    mide = size
    mid = size // 2

    if size == 0:
        return None

    while True:
        mide = mide // 2
        if (mid < size - 1 and
                list_integers[mid] < list_integers[mid + 1]):
            if mide // 2 == 0:
                mide = 2
            mid = mid + mide // 2
        elif mide > 0 and list_integers[mid] < list_integers[mid - 1]:
            if mide // 2 == 0:
                mide = 2
            mid = mid - mide // 2
        else:
            return list_integers[mid]
