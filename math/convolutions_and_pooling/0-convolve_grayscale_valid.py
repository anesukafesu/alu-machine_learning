#!/usr/bin/env python3
import numpy as np
""" Implements the convolve_grayscale_valid function
"""


def convolve_grayscale_valid(images, kernel):
    """ Function to perform a valid convolution on grayscale images
    Args:
        images (numpy.ndarray) a list of images in the shape (m, h, w)
        kernel (numpy.ndarray) an image in the shape of (kh, kw)
    """
    # Extract shape from images and kernel
    m, h, w = images.shape
    kh, kw = kernel.shape

    # Calculating convolved image dimensions
    oh = h - kh + 1
    ow = w - kw + 1

    # Creating an array of convolved images
    convolved_images = np.ones((m, oh, ow))

    # Loop through images applying kernel to calculate convolutions
    for i in range(oh):
        for j in range(ow):
            patch = images[:, i: i + kh, j: j + kw]
            convolved_images[i, j] = np.sum(patch * kernel)

    return convolved_images
