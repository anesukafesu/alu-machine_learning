#!/usr/bin/env python3
""" Implements the Multinormal class
"""
import numpy as np


class MultiNormal:
    """ Class to model a multivariate normal distribution
    """
    def __init__(self, data):
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError('data must be a 2D numpy.ndarray')

        _, n = data.shape

        if n < 2:
            raise ValueError('data must contain multiple data points')

        mean = np.mean(data, axis=1).reshape(1, -1)

        deviations = data - mean

        self.mean = mean
        self.cov = deviations @ deviations.T / (n - 1)