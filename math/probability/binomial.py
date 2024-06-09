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
            
            # Infer parameters from data

            # Calculate the sample mean = np
            sample_mean = sum(data) / len(data)

            # Calculate the sample variance = npq
            sample_variance = sum(map(lambda x: x ** 2, data)) / len(data) - sample_mean ** 2

            # q = npq / np = sample_variance / sample_mean
            q = sample_variance / sample_mean

            # q is the complement of p
            p = 1 - q

            # n = np / n = sample_mean / p
            n = round(sample_mean / p)

            # recalculate p since we rounded off n
            p = sample_mean / n

            # store the params
            self.n = n
            self.p = p

    def pmf(self, k):
        """ Calculates the PMF of a given number of successes
        Args:
            k (float | int): the number of successes whose pmf is to be determined
        Returns:
            p (float): the probability of k successes
        """
        k = int(k)
        
        if k < 0:
            return 0

        return self.__choose(self.n, k) * self.p ** k * (1 - self.p) ** (self.n - k)
    
    def cdf(self, k):
        """ Calculates the CDF of a given number of successes
        Args:
            k (float | int): the number of successes whose CDF is to be calculated
        Returns:
            p (float): the probability of successes from 0 through k (inclusive).
        """
        k = int(k)

        if k < 0:
            return 0
        
        return sum(map(lambda x: self.pmf(x), range(0, k + 1)))
    
    def __choose(self, n, k):
        """ Function that calculates the number of k combinations that can be made from n.
        Args:
            n (int): the size of the set from which combinations are to be drawn
            k (int): the size of each combination to be drawn from the set
        Returns:
            (int) the number of combinations that can be made
        """
        return self.__fact(n) / self.__fact(k) * self.__fact(n - k)
    
    def __fact(self, n):
        """ Calculates the factorial of a given number n.
        Args:
            n (int): the number whose factorial is to be calculated
        Returns:
            (int): the factorial of n
        """
        if not isinstance(n, int):
            raise TypeError('n must be an int')
        
        if n < 0:
            raise ValueError('n must be greater than or equal to zero')
        
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.__fact(n - 1)

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
