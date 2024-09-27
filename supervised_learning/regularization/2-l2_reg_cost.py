#!/usr/bin/env python3
""" Implements l2_reg_cost
"""
import tensorflow as tf


def l2_reg_cost(cost):
    """ Calculates the l2 cost of a tensorflow network.
    Parameters:
    cost (tensorflow.Tensor): a tensor representing the cost
    of the network without the l2 regularisation term.

    Returns:
    tensorflow.Tensor: a tensor representing the cost of the
    network with the l2 regularisation term.
    """
    return cost + tf.losses.get_regularization_losses()
