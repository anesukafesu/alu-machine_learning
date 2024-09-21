#!/usr/bin/env python3
""" Implements create_placeholders
"""
import tensorflow as tf


def create_placeholder(nx, classes):
    """ Creates x, y placeholders to hold inputs and
    outputs respectively:
    Args:
        nx (int) number of input neurons
        classes (int) number of classes
    Returns:
        (x, y) (tuple(tensorflow.Tensor)) the placeholders
        for inputs and outputs respectively.
    """
    x = tf.placeholder(tf.float32, shape=(1, nx))
    y = tf.placeholder(tf.float32, shape=(1, classes))

    return x, y