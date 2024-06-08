#!/usr/bin/env python3
""" Implements the Binomial Class
"""


class Binomial:
    """ Class to model a binomial distribution
    """
    def __init__(self, data=None, n=1, p=0.5):
        """Initialises the Binomial class
        Args:
            data (list[boolean] | none): Sample of values from distribution
            n (int | none): Number of trials
            p (float | none): The probability of success in each trial
        """
        if data is None:
            if n <= 0:
                raise ValueError('n must be a positive value')
            if p <= 0 or p >= 1:
                raise ValueError('p must be greater than 0 and less than 1')

            self.n = n
            self.p = p
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')

            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            
            mu = sum(data) / len(data)
            sigma = self.__sqrt(sum(map(lambda x: (x - mu) ** 2, data)) / len(data))
            q = sigma / mu
            p = 1 - q
            n = mu / p

            self.p = p
            self.n = round(n)

    def __sqrt(self, x):
        """ Function to calculate the square root of a given number x.
        """
        if x < 0:
            return complex(0, self.__sqrt(abs(x)))
        if x == 0:
            return 0
        n = 1
        last_n = 0
        while abs(last_n - n) > 0.00000001:
            last_n = n
            n = (n + x/n) * 0.5

        return n
