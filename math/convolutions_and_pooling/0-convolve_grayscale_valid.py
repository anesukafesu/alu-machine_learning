#!/usr/bin/env python3
import numpy as np


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
    ch = h - kh + 1
    cw = w - kw + 1

    # Creating an array of convolved images
    convolved_images = np.ones((m, ch, cw))

    # Loop through images applying kernel to calculate convolutions
    for i in range(ch):
        for j in range(cw):
            convolved_images[i, j] = np.sum(images[:, i: i + kh, j: j + kw] * kernel)

    return convolved_images