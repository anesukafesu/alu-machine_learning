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
    marked_predictions = tf.equal(tf.argmax(y, 1), tf.argmax(y_pred, 1))
    accuracy = tf.reduce_mean(tf.cast(marked_predictions, tf.float32))
    return accuracy
