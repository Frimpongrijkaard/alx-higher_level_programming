#!/usr/bin/python3
"""defines a list of finding peak in unsorted"""

def find_peak(list_of_integers):
    """Return a list of unsorted integers"""

    size = len(list_of_integers)
    mide = size
    mid = size // 2

    if size == 0:
        return None

    while True:
        mide = mide // 2
        if (mid < size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if mide // 2 == 0:
                mide = 2
            mid = mid + mide // 2
        elif mid_e > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if mide // 2 == 0:
                mide = 2
            mid = mid - mide // 2
        else:
            return list_of_integers[mid]
