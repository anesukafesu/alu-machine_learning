#!/usr/bin/env python3
""" Implements the Normal class
"""
class Normal:
    """ Represents a Normal or Gaussian distribution
    """
    def __init__(self, data=None, mean=0., stddev=1.):
        """ Initialises the Normal class
        Args:
            data (list | None): a sample of values of the distribution
            mean: the mean of the distribution
            stddev: the standard deviation of the distribution
        Returns:
            Normal: the distribution
        """
        if data is None:
            if stddev <= 0:
                raise ValueError('stddev must be a positive value')

            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')

            if len(data) < 2:
                raise ValueError('data must contain multiple values')

            self.mean = float(sum(data) / len(data))
            self.stddev = self.__sqrt(sum(map(lambda x: (x - mean) ** 2, data)) / (len(data) - 1))

    def __sqrt(self, x):
        """ Function to calculate the square root of a given number x.
        """
        if x < 0:
            return complex(0, self.__sqrt(-x))
        if x == 0:
            return 0
        n = 1
        last_n = 0
        while abs(last_n - n) > 0.0000001:
            last_n = n
            n = (n + x/n) * 0.5
    
        return n
