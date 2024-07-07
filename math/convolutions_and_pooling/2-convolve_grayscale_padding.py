#!/usr/bin/env python3
""" Implements the convolve_grayscale_padding function
"""
import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """ Function to perform a valid convolution on grayscale images.
    Convolved image will have same size as input images
    Args:
        images (numpy.ndarray) a list of images in the shape (m, h, w)
        kernel (numpy.ndarray) an image in the shape of (kh, kw)
    """
    # Extract padding
    ph, pw = padding

    # Apply padding
    padded_images = np.pad(images, ((0,), (ph,), (pw,)), mode='constant')

    # Extract shape from padded_images and kernel
    m, h, w = padded_images.shape
    kh, kw = kernel.shape

    # Calculate size of output images
    oh = h - kh + 1
    ow = w - kw + 1

    # Creating an array of convolved images
    convolved_images = np.zeros((m, oh, ow))

    # Loop through images applying kernel to calculate convolutions
    for i in range(oh):
        for j in range(ow):
            patch = padded_images[:, i: i + kh, j: j + kw]
            convolved_images[:, i, j] = np.sum(patch * kernel, axis=(1, 2))

    return convolved_images
