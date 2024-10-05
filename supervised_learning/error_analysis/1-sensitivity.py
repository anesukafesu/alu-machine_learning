#!/usr/bin/env python3
""" Implements create_confusion_matrix
"""
import numpy as np


def sensitivity(confusion_matrix):
    """ Calculate the sensitivity of each class in a given
    confusion matrix.

    Args:
        confusion_matrix (numpy.ndarray) The confusion matrix

    Returns:
        numpy.ndarray: The sensitivity of each class
    """
    true_positives = np.diag(confusion_matrix)
    true_positives_plus_false_negatives = np.sum(confusion_matrix, axis=1)
    return true_positives / true_positives_plus_false_negatives
