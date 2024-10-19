#!/usr/bin/env python3
""" Implements from_file
"""
import pandas as pd


def from_file(filename, delimiter):
    """ Reads data from a file and stores it in a DataFrame.
    Args:
        filename(str): The path to the file as a string.
        delimiter(str): The separator between columns used in
        the file.
    Returns:
        pandas.DataFrame: The data loaded into a dataframe.
    """
    return pd.read_csv(filename, sep=delimiter)