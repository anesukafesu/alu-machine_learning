#!/usr/bin/env python3
""" Implements the np_slice method
"""
import numpy as np

def np_slice(matrix, axes={}):
    """ Slices a matrix along specified axes and limits
    """
    result = matrix

    {}.items()

    for axis, slice_params in axes.items():
        # Extract the slice params
        start, end, step = extract_slice_params(slice_params)

        # Create indices to use to get data
        indices = np.arange(start, end, step)

        # Get rows from start to end using step
        result = np.take(result, indices, axis)

    return result


def extract_slice_params(slice_tuple):
    start = end = step = None

    # If only one value has been provided, it is the end value
    if len(slice_tuple) == 1:
        end, = slice_tuple

    # If two values have been provided, then they are the start and end values
    elif len(slice_tuple) == 2:
        start, end = slice_tuple

    # If three values have been provided, then they are the start, end and stop values
    elif len(slice_tuple) == 3:
        start, end, step = slice_tuple
    
    return start, end, step
