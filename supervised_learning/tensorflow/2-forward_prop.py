#!/usr/bin/env python3
""" Implements forward_prop
"""
import tensorflow as tf
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """ Performs forward propagation on a network with the
    parameters specified
    Args:
        x (tf.Tensor) the placeholder input data
        layer_sizes (List(int)) a list of integers where each
        number corresponds to the size of a layer
        activation_functions (List(int)) a list of activation functions 
        for each layer of the neural network
    Returns:
        predictions (tf.Tensor) the predictions made by the network
    """
    last_layer = x

    for layer_size, activation in zip(layer_sizes, activations):
        last_layer = create_layer(last_layer, layer_size, activation)

    return last_layer
