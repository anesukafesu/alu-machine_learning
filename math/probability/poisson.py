#!/usr/bin/env python3
""" Implements the Poisson Class
"""


class Poisson:
    """ Class to represent a Poisson Distribution
    """
    def __init__(self, data=None, lambtha=1.):
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

    def pmf(self, k):
        """ Calculates the probability that k events occur
        Args:
            k: the number of occurrences whose probability you want to calculate
        Returns:
            (float): the probability that k events are observed.
        """
        k = int(k)

        if k < 0:
            return 0
        else:
            e = 2.7182818285

            return e ** -self.lambtha * self.lambtha ** k / self.__fact(k)

    def cdf(self, k):
        """ Calculates the cumulative probability of zero occurrences up to and including k
        Args:
            k: the inclusive cutoff number of successes
        Returns:
            float: the comulative probability
        """
        k = int(k)

        if k < 0:
            return 0

        return sum(map(lambda i: self.pmf(i), range(k + 1)))

    def __fact(self, n):
        """ Calculates the factorial of a number.
        Args:
            n (int): The number whose factorial is to be calculated.
        Returns:
            (int): The factorial of n.
        """
        if not isinstance(n, int):
            raise TypeError('n must be an int')

        if n < 0:
            raise ValueError('n must be greater than or equal to zero')

        if n == 0 or n == 1:
            return 1
        else:
            return n * self.__fact(n - 1)
