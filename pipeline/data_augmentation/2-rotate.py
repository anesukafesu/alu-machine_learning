#!/usr/bin/env python3
""" Implements rotate_image
"""
import tensorflow as tf


def rotate_image(image):
  """ Rotates an image 90 degrees in the
  counter-clockwise direction.
  Args:
    image (tensorflow.Tensor): The image
    represented as a Tensor
  Returns:
    (tensorflow.Tensor): The flipped image.
  """
  return tf.image.rot90(image, k=1)