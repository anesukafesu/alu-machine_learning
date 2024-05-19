#!/usr/bin/env python3
""" Implements the np_slice method
"""

def np_slice(matrix, axes={}):
    """ Slices a matrix along specified axes and limits
    """
    result = matrix

    for axis, slice_params in axes.items():
        axis_length = matrix.shape[axis] - 1

        # Extract the slice params
        start, end, step = extract_slice_params(slice_params, axis_length)

        # Create indices to use to get data
        indices = list(range(start, end, step))

        # Get rows from start to end using step
        result = result.take(indices, axis)

    return result


def extract_slice_params(slice_tuple, axis_length):
    """ Extracts the slice parameters from the slice_tuple
    """
    start = 0
    end = axis_length
    step = 1

    # If only one value has been provided, it is the end value
    if len(slice_tuple) == 1:
        end = slice_tuple[0] or -1

    # If two values have been provided, then they are the start and end values
    elif len(slice_tuple) == 2:
        start, end = slice_tuple[0] or 0, slice_tuple[1] or axis_length

    # If three values have been provided, then they are the start, end and stop values
    elif len(slice_tuple) == 3:
        start, end, step = slice_tuple[0] or 0, slice_tuple[1] or axis_length, slice_tuple[2] or 1

    if step <= 0:
        return end, start - 1, step
    
    return start, end, step