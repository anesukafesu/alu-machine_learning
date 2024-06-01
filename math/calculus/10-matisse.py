#!/usr/bin/env python3
""" Implements the poly_derivative function
"""


def poly_derivative(poly):
    """ Calculates the derivative of a given polynomial
    """
    return list(map(lambda x, i: x * i, poly)[1:])
