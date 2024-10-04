#!/usr/bin/env python3
""" Implements create_confusion_matrix
"""
import numpy as np


def create_confusion_matrix(labels, logits):
    """ Creates a confusion matrix using labels and logits
    Args:
        labels (numpy.ndarray): A one-hot encoded numpy.ndarray
        containing the correct labels for each data point. The
        array is in the shape (m, classes) where m is the number
        of datapoints and classes is the number of classes in the
        dataset.

        logits (numpy.ndarray): A one-hot enocded numpy.ndarray
        containing the predictions made by the model for each
        data point. The array is in the shape (m, classes) where
        m is the number of data points and classes is the number
        of classes in the dataset.

    Returns:
        (numpy.ndarray) The confusion matrix of the model with
        the shape (classes, classes).
    """
    return labels.T @ logits
