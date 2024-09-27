#!/usr/bin/env python3
""" Implements reg_create_layer
"""
import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lam):
    """ Creates a tensorflow layer that includes l2
    regularization

    Parameters:
    prev (tensorflow.Tensor) Tensor containing the
    output of the previous layer.

    n (int) number of neurons that this layer should
    contain.

    activation (function) the activation function that
    the layer should use

    lam (float) the l2 regularization parameter that
    determines the strength of the regularization term.

    Returns:
    tensorflow.Tensor: the layer created
    """
    initializer = tf.contrib.layers.variance_scaling_initializer(
        mode="FAN_AVG")
    regularizer = tf.contrib.layers.l2_regularizer(lam)

    return tf.layers.Dense(n, activation=activation,
                           kernel_initializer=initializer,
                           kernel_regularizer=regularizer)(prev)
