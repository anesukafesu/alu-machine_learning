#!/usr/bin/env python3
""" Implements poly_integral function
"""


def poly_integral(poly, C=0):
    """ Calculates the integral of a given polynomial
    """
    if not isinstance(poly, list):
        return None

    if len(poly) == 0:
        return None

    if not __every(__is_number, poly):
        return None

    if not isinstance(C, int):
        return None

    powers = range(1, len(poly) + 1)

    integral = list(map(__divide, poly, powers))

    simplified_integral = __simplify_integral(integral)

    return [C] + simplified_integral


def __simplify_integral(coefficients):
    """ Simplifies integrals by trimming any trailing zeros
    from the coefficients list.
    """
    coefficients = coefficients.copy()

    while len(coefficients) >= 1 and coefficients[-1] == 0:
        coefficients.pop()

    return coefficients


def __divide(x, y):
    """ Divides x by y and returns the quotient.
    If the quotient is a whole number it will be returned
    as an int, else as a float
    """
    quotient = x / y

    if int(quotient) == quotient:
        return int(quotient)
    else:
        return quotient


def __is_number(x):
    """ Returns True if x is either an int or float
    """
    return isinstance(x, int) or isinstance(x, float)


def __every(func, iter):
    """ Returns True if each value in the iter returns True
    after being passed to func. Else it returns False
    """
    for val in iter:
        if not func(val):
            return False

    return True
