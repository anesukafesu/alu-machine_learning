#!/usr/bin/env python3
""" Implements the poly_derivative function
"""


def poly_derivative(poly):
    """ Calculates the derivative of a given polynomial
    """
    if not isinstance(poly, list):
        return None

    if not every(is_number, poly):
        return None

    if len(poly) == 0:
        return None

    if len(poly) == 1:
        return [0]

    return list(map(lambda x, i: x * i, poly, range(len(poly))))[1:]


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
