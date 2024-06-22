#!/usr/bin/env python3
""" Implements the likelihood method
"""
import numpy as np


def marginal(x, n, P, Pr):
    """ Function to calculate the marginal probability of P
    Args:
        x (int) the number of patients who develop side-effects
        n (int) the number of patients who have taken the drug
        P (numpy.ndarray) the list of different hypothetical probabilies
        Pr (numpy.ndarray) the list of different priors

    Returns:
        (float) marginal probability
    """
    __validate_params(x, n, P, Pr)
    return np.sum(__intersection(x, n, P, Pr))


def __validate_params(x, n, P, Pr):
    """ Function to validate parameters

    Args:
        x (int) the number of patients who develop side-effects
        n (int) the number of patients who have taken the drug
        P (numpy.ndarray) the list of different hypothetical probabilies
        Pr (numpy.ndarray) the list of different priors
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError('n must be a positive integer')

    if not isinstance(x, int) or x < 0:
        msg = 'x must be an integer that is greater than or equal to 0'
        raise ValueError(msg)

    if x > n:
        raise ValueError('x cannot be greater than n')

    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError('P must be a 1D numpy.ndarray')

    if not isinstance(Pr, np.ndarray) or P.shape != Pr.shape:
        raise TypeError('Pr must be a numpy.ndarray with the same shape as P')

    if not np.all((P >= 0) & (P <= 1)):
        raise ValueError('All values in P must be in the range [0, 1]')

    if not np.all((Pr >= 0) & (Pr <= 1)):
        raise ValueError('All values in Pr must be in the range [0, 1]')

    if not np.isclose(np.sum(Pr), 1):
        raise ValueError('Pr must sum to 1')


def __intersection(x, n, P, Pr):
    """ Calculates the intersection of obtaining data with various
    hypothetical probabilities
    Args:
        x (int) the number of patients who develop side-effects
        n (int) the number of patients who have taken the drug
        P (numpy.ndarray) the list of different hypothetical probabilies
        Pr (numpy.ndarray) the list of different priors
    """

    return Pr * __likelihood(x, n, P)


def __likelihood(x, n, P):
    """ Calculates the likelihood of obtaining data given
    different hypothetical probabilities. Assumes data has already
    been validated.
    Args:
        x (int) the number of patients who develop side-effects
        n (int) the number of patients who have taken the drug
        P (numpy.ndarray) the list of different hypothetical probabilites
            of developing side-effects.
    Returns:
        numpy.ndarray the list of different likelihoods
    """
    return __choose(n, x) * P ** x * (1 - P) ** (n - x)


def __choose(n, x):
    """ Calculates the number of combinations of x items that can
    be made by choosing values from a set of n items
    Args:
        n (int) the number of items to choose from
        x (int) the number of items to choose at a time
    Returns:
        (int) the number of combinations
    """
    return __fact(n) / (__fact(x) * __fact(n - x))


def __fact(n):
    """ Calculates the factorial of a given number n
    Args:
        n (int) the number whose factorial is to be calculated
    Returns:
        (int) the factorial of n
    """
    if not isinstance(n, int):
        raise TypeError('n is supposed to be an int')

    if n < 0:
        raise ValueError('n must be greater than or equal to zero')

    if n == 0 or n == 1:
        return 1
    else:
        return n * __fact(n - 1)
