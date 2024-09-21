#!/usr/bin/env python3
""" Implements calculate_loss
"""
import tensorflow as tf


def calculate_loss(y, y_pred):
    """ Calculates the loss of predictions made by the network
    Args:
        y (tf.Tensor) the correct classes for a given X
        y_pred (tf.Tensor) the predicted classes for said X
    Returns:
        loss (tf.Tensor) the loss of the predictions
    """
    return tf.nn.softmax_cross_entropy(logits=y_pred, onehot_labels=y)
