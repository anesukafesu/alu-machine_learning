#!/usr/bin/env python3
""" Implements the convolve_grayscale_valid function
"""
import numpy as np


def convolve_grayscale_same(images, kernel):
    """ Function to perform a valid convolution on grayscale images
    Args:
        images (numpy.ndarray) a list of images in the shape (m, h, w)
        kernel (numpy.ndarray) an image in the shape of (kh, kw)
    """
    # Extract shape from images and kernel
    m, h, w = images.shape
    kh, kw = kernel.shape

    # Calculate padding
    ph = kh - 1 // 2
    pw = kw - 1 // 2

    # Apply padding
    padded_images = np.pad(images, (ph, pw), mode='constant')

    # Creating an array of convolved images
    convolved_images = np.ones((m, h, w))

    # Loop through images applying kernel to calculate convolutions
    for i in range(h):
        for j in range(w):
            patch = padded_images[:, i: i + kh, j: j + kw]
            convolved_images[:, i, j] = np.sum(patch * kernel, axis=(1, 2))

    return convolved_images
