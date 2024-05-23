#!/usr/bin/env python3
""" implements the definiteness function
"""
import numpy as np


def definiteness(matrix):
    # Ensure it has rows
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    
    # Ensure it has columns
    if not isinstance(matrix[0], np.ndarray):
        return None
    
    # Ensure it is a square
    n_rows, n_cols = matrix.shape

    if n_rows != n_cols:
        return None
    
    # Ensure it is symmetrical
    matrix_tranposed = matrix.transpose()
    if not np.array_equal(matrix, matrix_tranposed):
        return None
    
    # Get the eigenvalues
    eigenvalues = np.linalg.eig(matrix)[0]

    # Check for definiteness
    if np.all(eigenvalues > 0):
        return 'Positive definite'
    
    if np.all(eigenvalues >= 0):
        return 'Positive semi-definite'
    
    if np.all(eigenvalues < 0):
        return 'Negative definite'
    
    if np.all(eigenvalues <= 0):
        return 'Negative semi-definite'
    
    if np.any(eigenvalues < 0) and np.any(eigenvalues > 0):
        return 'Indefinite'
    
    return None