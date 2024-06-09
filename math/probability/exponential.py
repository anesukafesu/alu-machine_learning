#!/usr/bin/env python3
""" Implements the Exponential class
"""


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

            self.lambtha = sum(data) / len(data)