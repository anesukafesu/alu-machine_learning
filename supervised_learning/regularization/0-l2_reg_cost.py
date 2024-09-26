#!/usr/bin/env python3
""" Implements the l2_reg_cost
"""
import numpy as np


def l2_reg_cost(cost, lam, weights, L, m):
    """Function to calculate the regularization cost of
    a neural network using L2 regularization.

    Parameters:
    cost (float): The cost of training the network
    without regularisation.

    lam (float): The regularisation parameter.

    weights (dict): The weights of the neural
    network organised as a dictionary with keys such
    as W1 for the weights of layer 1, w2 for layer 2 and
    numpy.ndarray for the associated weights.

    L (numpy.int): The number of layers in the neural
    network.

    m (numpy.int): The number of training examples in the
    neural network.

    Returns:
    numpy.float: The loss of the network accounting for
    l2 regularization.
    """

    weights = list(weights.values())
    sum_of_weights_squared = 0

    for layer_weights in weights.values():
        sum_of_weights_squared += np.sum(layer_weights ** 2)

    regularization_cost = (sum_of_weights_squared * lam) / (2 * m)

    # Returning the total loss
    return cost + regularization_cost