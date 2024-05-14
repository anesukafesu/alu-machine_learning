#!/usr/bin/env python3
import numpy as np
""" implements the np_cat function
"""


def np_cat(mat1, mat2, axis=0):
    """ concatenates np.ndarrays along a given axis
    default axis is 0
    """
    return np.concatenate((mat1, mat2), axis)
