#!/usr/bin/env python3
""" Implements the correlation function
"""
import numpy as np


def correlation(C):
    """ Calculates the correlation of different variables in a given
    covariance matrix.

    Args:
        C (numpy.ndarray) the covariance matrix with shape d x d
    Returns:
        (numpy.ndarray) the correlation matrix with shape d x d
    """
    if not isinstance(C, np.ndarray):
        raise TypeError('C must be a numpy.ndarray')

    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        raise ValueError('C must be a 2D square matrix') 

    stddevs = np.std(C, axis=0).reshape(1, -1)

    return C / (stddevs @ stddevs.T)
