#!/usr/bin/env python3
""" Implements specificity
"""
import numpy as np


def specificity(confusion_matrix):
    """ Calculates the specificity of each class for
    a given confusion matrix.

    Args:
        confusion_matrix (numpy.ndarray): The confusion
        matrix to be used in the calculations.

    Returns:
        numpy.ndarray: The specificity of each class
    """
    total_samples = np.sum(confusion_matrix)
    total_predictions_per_class = np.sum(confusion_matrix, axis=0)
    total_actuals_per_class = np.sum(confusion_matrix, axis=1)
    true_positives = np.diag(confusion_matrix)
    false_positives = total_predictions_per_class - true_positives
    true_negatives = (total_samples - total_predictions_per_class 
                      - total_actuals_per_class + true_positives)
    return true_negatives / (true_negatives + false_positives)
