#!/usr/bin/env python3
""" implements a the matrix_shape function
"""


def matrix_shape(matrix):
    """ determines the shape of a matrix
    params:
        matrix (a matrix object made using lists and ints)
    returns:
        list (representing the shape)
    """
    current_dimension = matrix
    shape = []

    while isinstance(current_dimension, list):
        shape.append(len(current_dimension))
        current_dimension = current_dimension[0]

    return shape
