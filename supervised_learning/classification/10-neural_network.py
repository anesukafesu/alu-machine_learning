#!/usr/bin/env python3
""" Module to implement NeuralNetwork
"""
import numpy as np


class NeuralNetwork:
    """ Class to implement a neural network
    """
    def __init__(self, nx, nodes):
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')

        if nx < 1:
            raise ValueError('nx must be a positive integer')

        if not isinstance(nodes, int):
            raise TypeError('nodes must be an integer')

        if nodes < 1:
            raise ValueError('nodes must be a positive integer')

        self.__W1 = np.random.normal(0, 1, (nodes, nx))
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.normal(0, 1, (1, nodes))
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        return self.__W1

    @property
    def b1(self):
        return self.__b1

    @property
    def A1(self):
        return self.__A1

    @property
    def W2(self):
        return self.__W2

    @property
    def b2(self):
        return self.__b2

    @property
    def A2(self):
        return self.__A2

    def __sigmoid(self, Z):
        """ Calculates the sigmoid of a number or numpy array
        Args:
            Z (numpy.ndarray): input either as a number or numpy.ndarray
        Return:
            Z (numpy.ndarray | numpy.float)
        """
        return 1 / (1 + np.exp(-Z))

    def forward_prop(self, X):
        """ Performs forward propagation in the network
        Args:
            X (numpy.ndarray with shape nx, m) where nx is
                number of input features and m is the number
                of training examples
        
        Returns:
            A1, A2 (numpy.ndarrays) the activations in layer
            1 and layer 2
        """
        # Calculating Z1
        # (nodes, nx) @ (nx, m) = (nodes, m)
        Z1 = self.__W1 @ X

        # Calculating activations in layer 1
        # (nodes, m)
        self.__A1 = self.__sigmoid(Z1)

        # Calculating Z2
        # (1, nodes) @ (nodes, m) = (1, m)
        Z2 = self.__W2 @ self.__A1

        # Calculating activations in layer 2
        self.__A2 = self.__sigmoid(Z2)

        return self.__A1, self.__A2
