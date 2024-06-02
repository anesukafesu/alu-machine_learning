#!/usr/bin/env python3
""" Implements the poly_derivative function
"""


def poly_derivative(poly):
    """ Calculates the derivative of a given polynomial
    """
    if not isinstance(poly, list):
        return None
    
    if len(poly) == 1:
        return [0]
    
    return list(map(lambda x, i: x * i, poly, range(len(poly))))[1:]
