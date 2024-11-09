#!/usr/bin/env python3
""" Implements change_hue
"""
import tensorflow as tf


def change_hue(image, delta):
  """ Adjusts the hue of an image.
  Args:
    image (tensorflow.Tensor): The image
    represented as a Tensor
    delta (float): How much to adjust the
    hue.
  Returns:
    (tensorflow.Tensor): The flipped image.
  """
  return tf.image.adjust_hue(image, delta)