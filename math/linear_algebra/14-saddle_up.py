#!/usr/bin/env python3
import numpy as np
""" implements the np_matmul function
"""


def np_matmul(mat1, mat2):
    """ Performs matrix multiplication on two np.ndarrays.
    Every row is multiplied by every column.
    """
    return mat1 @ mat2
