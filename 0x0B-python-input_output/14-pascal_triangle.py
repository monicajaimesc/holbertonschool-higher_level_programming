#!/usr/bin/python3
"""
Create a function
representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
    that returns a list of lists of integers
    Args:
        n (int): number of lines of triangle
    """

    big_list = []
    # Returns an empty list if n <= 0
    if n <= 0:
        # big list is empty
        return big_list
    else:
        for index_big_list in range(n):
            big_list.append([])
            if index_big_list == 0:
                big_list[index_big_list].append(1)
            else:
                prev_index_list = big_list[index_big_list - 1]
                current_list = big_list[index_big_list]
                for i, value in enumerate(prev_index_list):
                    if i == 0:
                        current_list.append(1)
                    else:
                        current_integer = prev_index_list[i]
                        previous_integer = prev_index_list[i - 1]
                        new_integer = current_integer + previous_integer
                        current_list.append(new_integer)
                current_list.append(1)
        return big_list
