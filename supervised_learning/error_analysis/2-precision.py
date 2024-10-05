#!/usr/bin/env python3
""" Implements create_confusion_matrix
"""
import numpy as np


def precision(confusion_matrix):
    """ Calculate the precision for each class of
    a given confusion matrix.

    Args:
        confusion_matrix (numpy.ndarray): The confusion matrix

    Returns:
        numpy.ndarray: The precision values
    """
    true_positives = np.diag(confusion_matrix)
    predicted_positives = np.sum(confusion_matrix, axis=0)
    return true_positives / predicted_positives
