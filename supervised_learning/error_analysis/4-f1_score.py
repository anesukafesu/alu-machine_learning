#!/usr/bin/env python3
""" Implements f1_score
"""
sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion_matrix):
    """ Calculates the f1 score for each class of a given
    confusion matrix
    Args:
        confusion_matrix (numpy.ndarray): The confusion matrix
    
    Returns:
        numpy.ndarray: The f1 scores
    """
    precision = precision(confusion_matrix)
    sensitivity = sensitivity(confusion_matrix)
    return (2 * precision * sensitivity) / (sensitivity + precision)
