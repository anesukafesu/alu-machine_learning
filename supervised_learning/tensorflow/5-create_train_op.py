#!/usr/bin/env python3
""" Implements create_train_op
"""
import tensorflow as tf


def create_train_op(loss, alpha):
    """ Creates a training operation for the network using
    gradient descent
    Args:
        loss (tf.Tensor) loss of the network’s prediction
        alpha (float) learning rate
    Returns:
        train_op: (tf.Operation) - operation to train the network
        using gradient descent
    """
    optimiser = tf.train.GradientDescentOptimizer(learning_rate=alpha)
    train_op = optimiser.minimize(loss)
    return train_op
