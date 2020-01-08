#!/usr/bin/python3
"""
Write a function that finds a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """finds a peak in an unsorted list of integers"""
    array = list_of_integers
    if array != []:
        array.sort()
        return array[-1]
    else:
        return None
