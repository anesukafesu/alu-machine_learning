#!/usr/bin/env python3
""" Implements crop_image
"""
import tensorflow as tf


def crop_image(image, size):
  """ Randomly crops an image using the
  provided size.
  Args:
    image (tensorflow.Tensor): The image
    represented as a Tensor
    size (tuple): The size of the crop
  Returns:
    (tensorflow.Tensor): The flipped image.
  """
  return tf.image.random_crop(image, size)