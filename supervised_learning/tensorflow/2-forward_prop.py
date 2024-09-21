#!/usr/bin/env python3
""" Implements forward_prop
"""
import tensorflow as tf
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activation_functions=[]):
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
    n_layers = len(layer_sizes)
    previous_layer = None

    # Building the neural network layer by layer
    for i in range(n_layers):
        layer_size = layer_sizes[i]
        activation_function = activation_functions[i]
        current_layer = None

        if previous_layer == None:
            current_layer = create_layer(x, layer_size, activation_function)
        else:
            current_layer = create_layer(previous_layer, layer_size, activation_function)

        previous_layer = current_layer

    # The final layer is the predictions layer
    predictions_layer = previous_layer
    return predictions_layer