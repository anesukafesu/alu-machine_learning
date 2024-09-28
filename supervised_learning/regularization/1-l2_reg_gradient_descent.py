#!/usr/bin/env python3
""" Implements l2_reg_gradient_descent
"""
import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lam, L):
    """ Updates the weights and biases of a neural network using
    gradients descent and l2 regularization. Weights and biases
    will be updated in place. Assumes tanh activation for each layer
    and softmax for the last layer.

    Parameters:
    Y (numpy.ndarray): A one-hot encoded numpy array with shape 
    (n_classes, m) that contains the correct labels for the data.
    In this context, n_classes is the number of classes and m is the
    number of training examples.

    weights (dict): Is a dictionary storing the weights of the neural
    network. It includes keys such as W1, W2 and b2 for the weights of
    layer 1, layer 2 and the bias of layer 2 respectively. It's values
    are numpy arrays storing the actual weights.

    cache (dict): Is a dictionary storing the outputs of each layer of
    the neural network. It contains keys such as A1, A2 for the
    activations of layer 1 and layer 2 respectively. It contains values
    as numpy arrays.

    alpha (float): The learning rate of the gradient descent algorithm.

    lam (float): The l2 regularization parameter.

    L (int): The number of layers in the neural network.

    Returns:
    None.
    """
    m = Y.shape[1]
    W_copy = weights.copy()

    for i in reversed(range(L)):
        A = cache["A" + str(i + 1)]
        if i == L - 1:
            dZ = cache["A" + str(i + 1)] - Y
            dW = (np.matmul(cache["A" + str(i)], dZ.T) / m).T
            dW_L2 = dW + (lam / m) * W_copy["W" + str(i + 1)]
            db = np.sum(dZ, axis=1, keepdims=True) / m
        else:
            dW2 = np.matmul(W_copy["W" + str(i + 2)].T, dZ2)
            tanh = 1 - (A * A)
            dZ = dW2 * tanh
            dW = np.matmul(dZ, cache["A" + str(i)].T) / m
            dW_L2 = dW + (lam / m) * W_copy["W" + str(i + 1)]
            db = np.sum(dZ, axis=1, keepdims=True) / m
        weights["W" + str(i + 1)] = (W_copy["W" + str(i+1)] - (alpha * dW_L2))
        weights["b" + str(i + 1)] = W_copy["b" + str(i + 1)] - (alpha * db)
        dZ2 = dZ