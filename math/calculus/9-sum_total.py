#!/usr/bin/env python3
""" Module that implements summation_i_squared
"""
import numpy as np


def summation_i_squared(n):
    """ Sums up the squares of all terms from 1 to n
    """
    nums = np.arange(1, n + 1)
    return np.sum(nums ** 2)
    