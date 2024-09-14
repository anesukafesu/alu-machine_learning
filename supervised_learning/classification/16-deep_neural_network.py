#!/usr/bin/env python3
""" Module to implement DeepNeuralNetwork
"""
import numpy as np


class DeepNeuralNetwork:
    """ A Deep Neural Network
    """
    def __init__(self, nx, layers):
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')

        if nx < 1:
            raise ValueError('nx must be a positive integer')

        if not isinstance(layers, list) or len(layers) == 0:
            raise TypeError('layers must be a list of positive integers')
        
        if not all(n > 0 for n in layers):
            raise TypeError('layers must be a list of positive integers')

        self.L = len(layers)
        cache = {}
        weights = {}

        for i in range(self.L):
            weights_key = 'W{}'.format(i + 1)
            biases_key = 'B{}'.format(i + 1)
            value = None

            if i == 0:
                value = self.he_initialization(nx, layers[i])
            else:
                value = self.he_initialization(layers[i - 1], layers[i])

            weights[weights_key] = value
            weights[biases_key] = 0

    def he_initialization(self, fan_in, fan_out):
        # Draw weights from a normal distribution with standard deviation sqrt(2/fan_in)
        return np.random.randn(fan_out, fan_in) * np.sqrt(2 / fan_in)