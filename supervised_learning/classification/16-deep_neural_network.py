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

        self.L = len(layers)
        self.cache = {}
        self.weights = {}
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

    def __he(fan_in, fan_out):
        # Draw weights from a normal distribution with standard deviation sqrt(2/fan_in)
        return np.random.randn(fan_out, fan_in) * np.sqrt(2 / fan_in)
