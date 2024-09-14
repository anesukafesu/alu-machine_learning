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

    def forward_prop(self, X):
        """ Performs forward propagation
        """
        self.__cache["A0"] = X
        for i in range(self.__L):
            W = self.__weights["W{}".format(i + 1)]
            b = self.__weights["b{}".format(i + 1)]
            A = self.__cache["A{}".format(i)]

            Z = np.matmul(W, A) + b
            self.__cache["A{}".format(i + 1)] = 1 / (1 + np.exp(-Z))

        return self.__cache["A{}".format(self.__L)], self.__cache

    def cost(self, Y, A):
        """ Calculates the cost of the model
        """
        m = Y.shape[1]
        cost = - (1 / m) * np.sum(Y * np.log(A) +
                                  (1 - Y) * np.log(1.0000001 - A))
        return cost
