#!/usr/bin/env python3
""" Implements the convolve_grayscale_valid function
"""
import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """ Convolves a set of images using kernel, padding and stride
    Args:
        images (numpy.ndarray) the set of images in shape m, h, w
        kernel (numpy.ndarray) the kernel to apply on the images
        padding (string | tuple) the padding to apply e.g. same, valid
            or a tuple with custom padding values
        stride (tuple) the stride to apply when convolving
    Returns:
        (numpy.ndarray) the set of convolved images
    """
    # Extract image and kernel shapes
    m, h, w = images.shape
    kh, kw = kernel.shape

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
    padded_images = np.pad(images, ((0,), (ph,), (pw,)), mode='constant', constant_values=0)

    # New image dimensions
    m, h, w = padded_images.shape

    # Calculate image output dimensions
    oh = calculate_output_size(h, kh, sh)
    ow = calculate_output_size(w, kw, sw)

    # Create the output image array
    convolved_images = np.zeros((m, oh, ow))

    # Convolve the images
    for i in range(oh):
        for j in range(ow):
            patch = padded_images[:, i * sh: i * sh + kh, j * sw: j * sw + kw]
            convolved_images[:, i, j] = np.sum(patch * kernel, axis=(1, 2))

    return convolved_images


def calculate_output_size(dimension_size, kernel_dize, stride):
    """ Calculates the size of the output after applying a convolution
    Args:
        dimension_size (int) The size of the dimension
        kernel_size (int) The size of the kernel in said dimension
        stride (int) The stride with which to move in the dimension
    Returns:
        (int) The size of the dimension after applyint the convolution
    """
    return (dimension_size - kernel_dize) // stride + 1


def calculate_padding_for_same_convolution(dimension_size, kernel_size, stride):
    """ Calculates the padding to be added to a dimension for a same convolution
    Args:
        dimension_size (int) The size of the dimension
        kernel_size (int) The size of the kernel in said dimension
        stride (int) The stride with which to move in the dimension
    Returns:
        (int) The padding to be applied to the dimension
    """
    return (stride * (dimension_size - 1) + kernel_size - dimension_size) // 2 + 1