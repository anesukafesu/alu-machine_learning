#!/usr/bin/env python3
"""
    A class DeepNeuralNetwork that defines a deep neural
    network performing binary classification
"""

import numpy as np


class DeepNeuralNetwork:
    """
    A class DeepNeuralNetwork
    """

    def __init__(self, nx, layers):
        ''' DeepNeuralNetwork class constructor'''
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(layers, list) or len(layers) == 0:
            raise TypeError("layers must be a list of positive integers")

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}
        self.nx = nx
        self.layers = layers

        # Initialize weights and biases and validate layers in one loop
        for i in range(self.__L):
            if not isinstance(layers[i], int) or layers[i] < 1:
                raise TypeError("layers must be a list of positive integers")
            if i == 0:
                self.__weights["W1"] = (
                    np.random.randn(layers[i], nx) * np.sqrt(2 / nx))
            else:
                self.__weights["W" + str(i + 1)] = np.random.randn(
                    layers[i], layers[i - 1]
                ) * np.sqrt(2 / layers[i - 1])
            self.__weights["b" + str(i + 1)] = np.zeros((layers[i], 1))

    # create the getter functions of the deep network
    @property
    def L(self):
        ''' return the L attribute'''
        return self.__L

    @property
    def cache(self):
        ''' return the cache attribute'''
        return self.__cache

    @property
    def weights(self):
        ''' return the weights attribute'''
        return self.__weights


#!/usr/bin/env python3
""" Implements DeepNeuralNetwork
"""

import numpy as np


class DeepNeuralNetwork:
    """ Creates a deep neural network
    """
    def __init__(self, nx, layers):
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')

        if nx < 1:
            raise ValueError('nx must be a positive integer')

        if not isinstance(layers, list) or len(layers) == 0:
            raise TypeError("layers must be a list of positive integers")

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}
        self.nx = nx
        self.layers = layers

        for i in range(self.L):
            if not isinstance(layers[i], int) or layers[i] < 1:
                raise TypeError("layers must be a list of positive integers")

            w_key = 'W{}'.format(i + 1)
            b_key = 'b{}'.format(i + 1)

            if i == 0:
                self.weights[w_key] = self.__he(nx, layers[i])
            else:
                self.weights[w_key] = self.__he(layers[i - 1], layers[i])

            self.weights[b_key] = np.zeros((layers[i], 1))

    def __he(self, fan_in, fan_out):
        """ Uses He et al algorithm
        """
        # Uses he algo to draw random weights
        return np.random.randn(fan_out, fan_in) * np.sqrt(2 / fan_in)

    @property
    def L(self):
        return self.__L

    @property
    def cache(self):
        return self.__cache

    @property
    def weights(self):
        return self.__weights
