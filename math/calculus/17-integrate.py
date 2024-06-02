#!/usr/bin/env python3
""" Implements poly_integral function
"""


def poly_integral(poly, C=0):
    """ Calculates the integral of a given polynomial
    """
    if not isinstance(poly, list):
        return None

    if not every(is_number, poly):
        return None

    powers = range(1, len(poly) + 1)

    return [C] + list(map(lambda x, p: x / p, poly, powers))

def is_number(x):
    """ Returns True if x is either an int or float
    """
    return isinstance(x, int) or isinstance(x, float)


def every(func, iter):
    """ Returns True if each value in the iter returns True
    after being passed to func. Else it returns False
    """
    for val in iter:
        if not func(val):
            return False

    return True
