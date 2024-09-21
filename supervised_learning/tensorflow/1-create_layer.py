#!/usr/bin/env python3
""" Implements create_layer
"""
import tensorflow as tf


def create_layer(prev, n, activation):
    """ Creates a dense layer for a neural network
    Args:
        prev (tf.Tensor) the previous layer's tensor
        n (int) the number of nodes in the current layer
        activation (function) the activation the layer should use
    Returns:
        layer (tf.Tensor) the layer
    """
    initialiser = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    return tf.layers.dense(prev, units=n, activation=activation,
                            kernel_initializer=initialiser, name='layer')
