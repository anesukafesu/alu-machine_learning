#!/usr/bin/env python3
""" Implements the np_slice method
"""

def np_slice(matrix, axes={}):
    """
    Slices a matrix along specific axes.

    Args:
    - matrix (list of lists): The matrix to slice.
    - axes (dict): A dictionary where the key is an axis to slice along
      and the value is a tuple representing the slice to make along that axis.

    Returns:
    - list of lists: The sliced matrix.
    """
    sliced_matrix = matrix.copy()
    for axis, slice_tuple in axes.items():
        axis_index = axis % len(matrix)  # Ensure the axis index is within the range of dimensions
        start, stop, step = extract_slice_params(slice_tuple)
        sliced_matrix = [row[start:stop:step] if i == axis_index else row for i, row in enumerate(sliced_matrix)]
    return sliced_matrix


def extract_slice_params(slice_tuple):
    start = end = step = None

    # If only one value has been provided, it is the end value
    if len(slice_tuple) == 1:
        end = slice_tuple[0] or -1

    # If two values have been provided, then they are the start and end values
    elif len(slice_tuple) == 2:
        start, end = slice_tuple[0] or 0, slice_tuple[1] or -1

    # If three values have been provided, then they are the start, end and stop values
    elif len(slice_tuple) == 3:
        start, end, step = slice_tuple[0] or 0, slice_tuple[1] or -1, slice_tuple[2] or 1
    
    return start, end, step
