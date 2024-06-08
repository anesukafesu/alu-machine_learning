#!/usr/bin/env python3
""" Implements the Normal class
"""
π = 3.1415926536
e = 2.7182818285


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

            # Calculating mean
            self.mean = float(sum(data) / len(data))

            # Calulcating standard deviation
            numerator = sum(map(lambda x: (x - self.mean) ** 2, data))
            variance = numerator / (len(data))
            self.stddev = self.__sqrt(variance)

    def z_score(self, x):
        """ Calculates z-score of a given x value
        Args:
            x (float | int) the value whose z-score is to be calculated
        Returns:
            z (float) the z value of x
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """ Calculates the x value given a z-score
        Args:
            z (float | int) the z-score whose x value is to be calculated
        Returns:
            x (float) the x value of the given z-score
        """
        return self.mean + z * self.stddev

    def pdf(self, x):
        """ Calculates the PDF of a given x in the normal distribution
        Params:
            x (float | int)
        Returns:
            pdf(float | int)
        """
        z_score = self.z_score(x)

        numerator = e ** (-(z_score ** 2) / 2)
        denominator = self.stddev * self.__sqrt(2 * π)

        return numerator / denominator

    def cdf(self, x):
        """ Calculates the cdf of a given x in the normal distribution.
        Params:
            x (float | int) the upper limit
        Returns:
            (float | int) the cumulative probability
        """
        # This function requires integration, which we are not going to do
        # Instead we will approximate the area under the function by
        # 1. Sampling the function at different points
        # 2. Calculating the height at each of these points using the self.pdf
        # 3. Multiply the height of each point with the interval_width to get approximate area
        # 4. Add up these areas to get approximate total area under the curve
        # To do this, we need two parameters, a lower bound for integration since 
        # starting from -infinity is impractical and computationally expensive
        # The lower the lower_bound, the more accurate the approximation, but with diminishing
        # returns.
        # We also need an interval_width that determines the sample frequency.
        # The lower the frequency, the more accurate the approximation, also with diminishing
        # returns
        parameters = {
            'interval_width': 0.0001,
            'lower_bound': -10,
        }

        lower_x_value = self.x_value(parameters['lower_bound'])
        samples = range(lower_x_value, x, parameters['interval_width'])
        return sum(map(lambda z: self.pdf(z) * parameters['interval_width'], samples))

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
