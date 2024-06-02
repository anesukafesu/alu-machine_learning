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
    
    # Edge cases
    if len(poly) == 1 and poly[0] == 0:
        return [C]

    powers = range(1, len(poly) + 1)

    def divide_by_power(x, p):
        quotient = x / p

        if int(quotient) == quotient:
            return int(quotient)
        else:
            return quotient

    return [C] + list(map(divide_by_power, poly, powers))


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
