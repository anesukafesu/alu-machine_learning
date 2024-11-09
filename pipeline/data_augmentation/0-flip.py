#!/usr/bin/env python3
""" Implements flip_image
"""
import tensorflow as tf


def flip_image(image):
  """ Flips an image from left to right.
  Args:
    image (tensorflow.Tensor): The image
    represented as a Tensor
  Returns:
    (tensorflow.Tensor): The flipped image.
  """
  return tf.image.flip_left_right(image)