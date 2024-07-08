#!/usr/bin/env python3
""" Implements the convolve_channels function
"""
import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """ Convolves a set of multi-channel images using different
    multiple kernels, padding, and stride
    Args:
        images (numpy.ndarray) the set of images in shape m, h, w, c
        kernel (numpy.ndarray) the kernel to apply on the images
        padding (string | tuple) the padding to apply e.g. same, valid
            or a tuple with custom padding values
        stride (tuple) the stride to apply when convolving
    Returns:
        (numpy.ndarray) the set of convolved images
    """
    # Extract image and kernel shapes
    m, h, w, c = images.shape
    kh, kw, kc, nk = kernels.shape

    # Extract stride values
    sh, sw = stride

    # Initialise padding to zero
    ph = pw = 0

    # Calculate the amount of padding to use
    if padding == 'same':
        ph = calculate_padding_for_same_convolution(h, kh, sh)
        pw = calculate_padding_for_same_convolution(w, kw, sw)
    elif isinstance(padding, tuple):
        ph, pw = padding

    # Pad the images
    padded_images = np.pad(images, ((0,), (ph,), (pw,), (0,)))

    # New image dimensions
    m, h, w, c = padded_images.shape

    # Calculate image output dimensions
    oh = calculate_output_size(h, kh, sh)
    ow = calculate_output_size(w, kw, sw)

    # Create the output image array
    convolved_images = np.zeros((m, oh, ow, nk))

    # Loop through each kernel
    for i in range(nk):
        # Convolve the images
        for j in range(0, oh * sh, sh):
            for k in range(0, ow * sw, sw):
                patch = padded_images[:, j: j + kh, k: k + kw, :]
                element = np.sum(patch * kernels[:, :, :, i], axis=(1, 2, 3))
                convolved_images[:, j // sh, k // sw, i] = element

    return convolved_images


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


def calculate_padding_for_same_convolution(n, k, s):
    """ Calculates the padding to be added to a dimension
    for a same convolution
    Args:
        n (int) The size of the dimension
        k (int) The size of the kernel in said dimension
        s (int) The stride with which to move in the dimension
    Returns:
        (int) The padding to be applied to the dimension
    """
    return (s * (n - 1) + k - n) // 2 + 1
