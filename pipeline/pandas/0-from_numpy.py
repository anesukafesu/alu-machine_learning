#!/usr/bin/env python3
""" Implements from_numpy
"""
import pandas as pd


def from_numpy(array):
    """ Creates a pandas DataFrame from a NumPy array.
    Args:
        array (numpy.ndarray) The NumPy array to convert.
    Returns:
        pandas.DataFrame: The dataframe with entries from
        array.
    """
    nx = array.shape[1]
    columns = list(map(lambda n: chr(n), range(65, 65 + nx)))
    df = pd.DataFrame(array)
    df.columns = columns
    return df