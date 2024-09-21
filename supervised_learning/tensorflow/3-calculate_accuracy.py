#!/usr/bin/env python3
""" Implements calculate_accuracy
"""
import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """ Calculates the accuracy of predictions made by the network
    Args:
        y (tf.Tensor) the correct classes for a given X
        y_pred (tf.Tensor) the predicted classes for said X
    Returns:
        accuracy (tf.Tensor) the accuracy of the predictions
    """
    marked_predictions = tf.cast(tf.argmax(y) == tf.argmax(y_pred), tf.float32)
    accuracy = tf.reduce_mean(marked_predictions)
    return accuracy