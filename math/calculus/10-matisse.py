#!/usr/bin/env python3
""" Implements the poly_derivative function
"""


def poly_derivative(poly):
    """ Calculates the derivative of a given polynomial
    """
    return list(map(poly, lambda x, i: x * i)[1:])
