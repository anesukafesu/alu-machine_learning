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
        # (nodes, nx) @ (nx, m) + (nodes, 1)[broadcast to (nodes, m)]
        # = (nodes, m)
        Z1 = self.__W1 @ X + self.__b1

        # Calculating activations in layer 1
        # (nodes, m)
        self.__A1 = self.__sigmoid(Z1)

        # Calculating Z2
        # (1, nodes) @ (nodes, m) + (1, 1)[Broadcast to (1, m)] = (1, m)
        Z2 = self.__W2 @ self.__A1 + self.__b2

        # Calculating activations in layer 2
        # (1, m)
        self.__A2 = self.__sigmoid(Z2)

        return self.__A1, self.__A2

    def cost(self, Y, A):
        """ Calculates the cost of the model.
        Args:
            Y (numpy.ndarray) with shape (1, m) the correct output labels
            A (numpy.ndarray) with shape (1, m) the predicted output labels
        Returns:
            (numpy.float) the cost of the model
        """
        _, m = Y.shape

        costs = Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)
        cost = (-1 / m) * np.sum(costs)
        return cost

    def evaluate(self, X, Y):
        """ Evaluates the model
        Args:
            X (numpy.ndarray) with the shape (nx, m) the input data
            Y (numpy.ndarray) with the shape (1, m) the correct labels for
            the data
        Returns:
            (Y_hat, cost) the predictions of the model and the cost
        """
        # Make predictions
        _, A = self.forward_prop(X)

        # Calculate the cost
        cost = self.cost(Y, A)

        # Categorise predictions
        Y_hat = np.where(A >= 0.5, 1, 0)

        return Y_hat, cost

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """ Perform one pass of gradient descent to update weights and bias
        """
        _, m = Y.shape
        dz2 = A2 - Y
        dw2 = (1 / m) * np.dot(dz2, A1.T)
        db2 = (1 / m) * np.sum(dz2, axis=1, keepdims=True)

        dz1 = np.dot(self.__W2.T, dz2) * (A1 * (1 - A1))
        dw1 = (1 / m) * np.dot(dz1, X.T)
        db1 = (1 / m) * np.sum(dz1, axis=1, keepdims=True)

        self.__W2 -= (alpha * dw2)
        self.__b2 -= (alpha * db2)

        self.__W1 -= (alpha * dw1)
        self.__b1 -= (alpha * db1)

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """ Trains the model using gradient descent
        Args:
            X is a numpy.ndarray with shape (nx, m)
            that contains the input data
            nx is the number of input features to the neuron
            m is the number of examples
            Y is a numpy.ndarray with shape (1, m)
            that contains the correct labels for the input data
            iterations is the number of iterations to train over
            alpha is the learning rate
        """
        if not isinstance(iterations, int):
            raise TypeError('iterations must be an integer')

        if iterations <= 0:
            raise ValueError('iterations must be a positive integer')

        if not isinstance(alpha, float):
            raise TypeError('alpha must be a float')

        if alpha <= 0:
            raise ValueError('alpha must be positive')

        for _ in range(iterations):
            A1, A2 = self.forward_prop(X)
            self.gradient_descent(X, Y, A1, A2, alpha)

        # evaluate the gradient descent
        evaluation = self.evaluate(X, Y)
        return evaluation
