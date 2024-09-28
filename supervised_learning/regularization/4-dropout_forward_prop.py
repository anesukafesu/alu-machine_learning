#!/usr/bin/env python3
""" Implements the dropout_forward_prop function
"""
import numpy as np


def dropout_forward_prop(X, weights, L, keep_prob):
    """Performs forward propagation with dropout

    Args:
        X (numpy.ndarray): The input x in the shape (nx, m)
        where nx is the number of input features and m is
        the number of training examples.

        weights (dict): A dictionary containing the weights
        and biases of each layer where the key is W1 for
        the weights of layer 1 and b1 for the bias of
        layer 1. And the values are numpy.ndarrays holding
        the actual weights.

        L (int): The number of layers in the network.

        keep_prob (float): The probability that a neuron is
        kept, i.e. not dropped.

    Returns:
        tuple: A tuple containing the activations of each
        layer and the dropout mask used for each layer.
    """
    cache = {}
    cache['A0'] = X

    for i in range(1, L + 1):
        # Get previous layer's activations as input
        X = cache['A' + str(i - 1)]

        # Get this layer's weights
        W = weights['W' + str(i)]

        # Get this layer's bias
        b = weights['b' + str(i)]

        # Calculate z = wx + b
        Z = W @ X + b

        # Apply activation
        if i == L:
            # If it's the last layer, we apply softmax activation
            t = np.exp(Z)
            A = t / np.sum(t, axis=0, keepdims=True)
            cache['A' + str(i)] = A
        else:
            # If it's not the last layer, we apply tanh activation
            # Then drop some neurons
            A = np.tanh(Z)

            # Generate a drop max of ones and zeros where the prob
            # of a 1 is keep_prob.
            random_values = np.random.rand(A.shape[0], A.shape[1])
            D = (random_values > keep_prob).astype(int)

            # Apply the mask
            A *= D

            A /= keep_prob

            cache['A' + str(i)] = A
            cache['D' + str(i)] = D

    return cache
        