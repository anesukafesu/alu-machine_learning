#!/usr/bin/env python3


def matrix_transpose(matrix):
    # n is the number of rows in the transposed matrix
    transposed_matrix = []
    n = len(matrix[0])

    for i in range(n):

        new_row = []

        for row in matrix:
            new_row.append(row[i])
        
        transposed_matrix.append(new_row)
    
    return transposed_matrix
