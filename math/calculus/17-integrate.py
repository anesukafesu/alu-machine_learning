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

    integral = list(map(divide, poly, powers))

    return [C] + simplify_integral(integral)


def simplify_integral(coefficients):
    """ Simplifies integrals by trimming any trailing zeros
    """
    while coefficients[-1] and coefficients[-1] == 0:
        coefficients.pop()

    return coefficients


def divide(x, y):
    """ Divides x by y and returns the quotient.
    If the quotient is a whole number it will be returned
    as an int, else as a float
    """
    quotient = x / y

    if int(quotient) == quotient:
        return int(quotient)
    else:
        return quotient


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
