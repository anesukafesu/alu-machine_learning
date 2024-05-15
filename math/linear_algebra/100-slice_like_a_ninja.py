#!/usr/bin/env python3
""" Implements the np_slice method
"""

def np_slice(matrix, axes={}):
    """ Slices a matrix along specified axes and limits
    """
    zero = axes.get(0)
    one = axes.get(1)
    result = matrix

    if zero is not None:
        # Extract the parameters for the slice
        start, end, step = extract_slice_params(zero)

        # Get rows from start to end using step
        result = result[start: end: step]
        

    if one is not None:
        # Extract the parameters for the slice
        start, end, step = extract_slice_params(one)

        # Get columns from start to end using step
        result = result[:, start: end: step]

    return result


def extract_slice_params(slice_tuple):
    start = end = step = None

    if len(slice_tuple) == 1:
        end, = slice_tuple
    elif len(slice_tuple) == 2:
        start, end = slice_tuple
    elif len(slice_tuple) == 3:
        start, end, step = slice_tuple
    
    return start, end, step
