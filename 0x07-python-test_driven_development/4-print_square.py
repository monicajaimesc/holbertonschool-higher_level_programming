#!/usr/bin/python3
"""
Print Square module, for printing squares with "#".

useful for all square-based applications
"""


def print_square(size):
    """size is the size length of the square
    size must be an integer
    """

    # size must be an integer, otherwise raise a TypeError
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    # if size is less than 0, raise a ValueError
    if size < 0:
        raise ValueError('size must be >= 0')
    # size is equal to lado por lado

    for x in range(size):
        print('#' * size)
