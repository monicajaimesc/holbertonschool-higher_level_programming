#!/usr/bin/python3
"""
This is the divide module.
has a function to divide matrix
Divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """matrix must be a list of lists of integers/floats
    Returns a new matrix
    """
    newmatrix = []
    length = 0

    # Divides all elements of a matrix
    if isinstance(div, int) is False and isinstance(div, float) is False:
        raise TypeError('div must be a number')
    # Matrix must be a list of integers or floats, TypeError
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if not isinstance(matrix[0], list):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    # matix has to exist, can't be less or equal to 0
    if len(matrix[0]) <= 0:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    # 1.let's create new matrix with newrow
    for row in matrix:
        newrow = []
        # matrix must be a list
        if type(row) is not list:
            raise TypeError('matrix must be a matrix (list of lists) '
                            'of integers/floats')
        # 2. row is empty
        if length is 0:
            length = len(row)
        # Each row must be the same size, TypeError
        elif len(row) is not length:
            raise TypeError('Each row of the matrix must have the same size')
        # 3. each item has to be an integer or float
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError('matrix must be a matrix (list of lists) '
                                'of integers/floats')
            # 4. add content to the row
            # elements will be divided by div and rounded with 2 decimal
            # round() function returns a floating point number that is
            # a rounded version of the specified number
            # with the specified number of decimals
            newrow.append(round(item / div, 2))
        # add content to the matrix
        newmatrix.append(newrow)
    return newmatrix
