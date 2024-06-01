#!/usr/bin/env python3
""" Implements the poly_derivative function
"""
import numpy as np


def poly_derivative(poly):
    """ Calculates the derivative of a given polynomial
    """
    p = np.array(poly)
    powers = np.arange(p.size)

    return (p * powers)[1:]
