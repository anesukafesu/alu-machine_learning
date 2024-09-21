#!/usr/bin/env python3
""" Implements create_placeholders
"""
import tensorflow as tf


def create_placeholders(nx, classes):
    """ Creates x, y placeholders to hold inputs and
    outputs respectively:
    Args:
        nx (int) number of input neurons
        classes (int) number of classes
    Returns:
        (x, y) (tuple(tensorflow.Tensor)) the placeholders
        for inputs and outputs respectively.
    """
    x = tf.placeholder(tf.float32, shape=(None, nx), name='x')
    y = tf.placeholder(tf.float32, shape=(None, classes), name='y')

    return x, y
