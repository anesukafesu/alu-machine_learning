#!/usr/bin/env python3
""" Implements the likelihood method
"""
import numpy as np


def likelihood(x, n, P):
    """ Calculates the likelihood of obtaining data given
    different hypothetical probabilities
    Args:
        x (int) the number of patients who develop side-effects
        n (int) the number of patients who have taken the drug
        P (numpy.ndarray) the list of different hypothetical probabilites 
            of developing side-effects.
    Returns:
        numpy.ndarray the list of different likelihoods
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError('n must be a positive integer')

    if not isinstance(x, int) or x < 0:
        raise ValueError('x must be an integer that is greater than or equal to 0')

    if x > n:
        raise ValueError('x cannot be greater than n')

    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError('P must be a 1D numpy.ndarray')

    if not np.all(P >= 0 and P <= 1):
        raise ValueError('All values in P must be in range [0, 1]')

    return np.choose(n, x) * P ** x * (1 - P) ** (n - x)