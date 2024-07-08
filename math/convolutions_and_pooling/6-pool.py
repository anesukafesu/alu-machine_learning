#!/usr/bin/env python3
""" Implements the pool function
"""
import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """ Function to perform pooling on a set of images
    Args:
        images (numpy.ndarray) the set of images as a numpy array
        kernel_shape (tuple) the shape of the kernel to be used
            to get numbers from the kernel
        stride (tuple) the stride by which to move
        mode ('max' | 'avg') the mode by which to perform the pooling
    """
    # Extract the image shape
    m, h, w, c = images.shape

    # Extract the kernel shape
    kh, kw = kernel_shape

    # Extraact the stride
    sh, sw = stride

    # Calculate the output size
    oh = calculate_output_size(h, kh, sh)
    ow = calculate_output_size(w, kw, sw)

    # Create the output array
    pooled_images = np.zeros((m, oh, ow, c))

    # Pool the images
    for i in range(0, oh * sh, sh):
        for j in range(0, ow * sw, sw):
            patch = images[:, i: i + kh, j: j + kw, :]
            result = 0

            if mode == 'max':
                result = np.max(patch, axis=(1, 2))
            elif mode == 'avg':
                result = np.average(patch, axis=(1, 2))

            pooled_images[:, i // sh, j // sw, :] = result

    return pooled_images


def calculate_output_size(n, k, s):
    """ Calculates the size of the output after applying a convolution
    Args:
        n (int) The size of the dimension
        k(int) The size of the kernel in said dimension
        s (int) The stride with which to move in the dimension
    Returns:
        (int) The size of the dimension after applyint the convolution
    """
    return (n - k) // s + 1
