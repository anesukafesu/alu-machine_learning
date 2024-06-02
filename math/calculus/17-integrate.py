#!/usr/bin/env python3
""" Implements poly_integral function
"""


def poly_integral(poly, C=0):
    """ Calculates the integral of a given polynomial
    """
    if not isinstance(poly, list):
        return None

    if not isinstance(poly, int) or not isinstance(poly, float):
        return None

    powers = range(1, poly.len + 1)

    return [C] + map(lambda x, p: x / p, poly, powers)
