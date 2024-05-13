#!/usr/bin/env python3


def matrix_shape(matrix):
    current_dimension = matrix
    shape = []

    while isinstance(current_dimension, list):
        shape.append(len(current_dimension))
        current_dimension = current_dimension[0]

    return shape