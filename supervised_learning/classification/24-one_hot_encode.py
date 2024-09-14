#!/usr/bin/env python3
""" Module to implement one_hot_encode
"""
import numpy as np


def one_hot_encode(Y, classes):
    """ Performs one hot encoding
    Args:
        Y: the vector with the classes
        classes: the maximum number of classes
    Result:
        numpy.ndarray | None
    """
    if not isinstance(Y, np.ndarray):
        return None
    if not isinstance(classes, int):
        return None

    try:
        result = np.eye(classes)[Y].T
        return result
    except Exception:
        return None
