#!/usr/bin/env python3
""" Module to implement one_hot_encode
"""
import numpy as np


def one_hot_encode(Y, classes):
    encoded_Y = []
    label_lookup = {}
    labels_so_far = 0

    for label in Y:
        if not label in label_lookup:
            n_prefix_zeros = labels_so_far
            n_suffix_zeros = classes - labels_so_far - 1
            vector = [0] * n_prefix_zeros + [1] + [0] * n_suffix_zeros

            label_lookup[label] = vector
            labels_so_far += 1

        vector = label_lookup[label]
        encoded_Y.append(vector)

    return np.array(encoded_Y)
