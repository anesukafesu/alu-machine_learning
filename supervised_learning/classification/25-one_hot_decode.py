#!/usr/bin/env python3
""" Module to implement one_hot_encode
"""
import numpy as np


def one_hot_decode(one_hot):
    """ Performs one hot decoding
    Args:
        one_hot: a one hot encoded matrix
    Result:
        numpy.ndarray | None
    """
    if not isinstance(one_hot, np.ndarray):
        return None

    if one_hot.ndim != 2:
        return None

    return one_hot.T.argmax(axis=1)
