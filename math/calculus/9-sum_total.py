#!/usr/bin/env python3
""" Module that implements summation_i_squared
"""


def summation_i_squared(n):
    """ Sums up the squares of all terms from 1 to n
    """
    if not isinstance(n, int) or n <= 0:
        return None

    return sum(map(lambda x: x ** 2, range(1, n + 1)))
