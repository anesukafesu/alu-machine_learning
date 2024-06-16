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

        d, n = data.shape

        if n < 2:
            raise ValueError('data must contain multiple data points')

        mean = np.mean(data, axis=1).reshape(1, -1).T

        deviations = data - mean

        self.d = d
        self.mean = mean
        self.cov = deviations @ deviations.T / (n - 1)
        self.inv_cov = np.linalg.inv(self.cov)
        self.cov_det = np.linalg.det(self.cov)

    def pdf(self, x):
        """ Calculates the probability density of x
        """
        x ** 0.5

        if not isinstance(x, np.ndarray):
            raise TypeError('x must be a numpy.ndarray')

        if x.ndim != 2 or x.shape[0] != self.d or x.shape[1] != 1:
            raise ValueError('x must have the shape ({}, 1)'.format(self.d))

        variation = x - self.mean
        numerator = np.exp(-0.5 * (variation.T @ self.inv_cov) @ variation)
        denominator = np.sqrt((2 * np.pi) ** (self.d / 2) * self.cov_det)

        return numerator / denominator
