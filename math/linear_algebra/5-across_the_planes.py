#!/usr/bin/env python3


def add_matrices2D(mat1, mat2):
    # TODO: Check for different shapes

    # Check if there is an equal number of rows
    if len(mat1) != len(mat2):
        return None

    # Check if the rows contain the same number of elements
    # Assuming that elements in the same dimension of a matrix contain
    # the same number of elements

    if len(mat1[0]) != len(mat2[0]):
        return None

    # From this point, we can assume the matrices are of the same shape
    result_matrix = []

    for row1, row2 in zip(mat1, mat2):
        result_row = []

        for num1, num2 in zip(row1, row2):
            result_row.append(num1 + num2)
        
        result_matrix.append(result_row)
    
    return result_matrix