#!/usr/bin/env python3
""" Implements change brightness
"""
import tensorflow as tf


def change_brightness(image, max_delta):
  """ Randomly changes the brightness of an image.
  Args:
    image (tensorflow.Tensor): The image
    represented as a Tensor
    max_delta (float): The maximum change to make.
  Returns:
    (tensorflow.Tensor): The flipped image.
  """
  return tf.image.random_brightness(image, max_delta=max_delta)