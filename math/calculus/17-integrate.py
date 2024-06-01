#!/usr/bin/env python3
""" Implements poly_integral function
"""


def poly_integral(poly):
    """ Calculates the integral of a given polynomial
    """
    return [0] + list(map(lambda x, i: x / (i + 1), poly))
