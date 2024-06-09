#!/usr/bin/env python3
""" Implements the Exponential class
"""
e = 2.7182818285


class Exponential:
    """ Class to model an exponential distribution
    """
    def __init__(self, data=None, lambtha=1.):
        """ Initialise Exponential class
        Args:
            data (list[float] | None): A sample of values from
            which the parameter lambda can be derived
            lambtha (float): The parameter lambda
        Returns:
            Exponential
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')

            if len(data) < 2:
                raise ValueError('data must contain multiple values')

            self.lambtha = len(data) / sum(data)

    def pdf(self, x):
        """ Calculates the pdf of a given value x
        Args:
            x (float): the value whose pdf is to be calculated
        Returns:
            (float): the pdf of x
        """
        if x < 0:
            return 0
        else:
            return self.lambtha * e ** (-self.lambtha * x)
        
    def cdf(self, x):
        """ Calculates the cdf of a given x value
        Args:
            x (float): the value whose cdf is to be calculated
        Returns:
            (float): the cdf of x
        """
        if x < 0:
            return 0
        else:
            return 1 - e ** (-self.lambtha * x)
