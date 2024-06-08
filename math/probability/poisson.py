#!/usr/bin/env python3
""" Implements the Poisson Class
"""


class Poisson:
    """ Class to represent a Poisson Distribution
    """
    def __init__(self, data=None, lambtha = 1.):
        """ Initialise the Poisson Class
        Args:
            data list[int] | None
            lambtha float | None
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            self.lambtha = lambtha
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            
            if len(data) < 2:
                raise ValueError('data must contain multiple values')

            self.lambtha = float(sum(data) / len(data))