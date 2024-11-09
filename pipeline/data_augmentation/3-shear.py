#!/usr/bin/env python3
""" Implements shear_image
"""
import tensorflow as tf


def shear_image(image, intensity):
  """ Randomly shears an image with the provided intensity.
  Args:
    image (tensorflow.Tensor): The image represented as a
    Tensor
  Returns:
    (tensorflow.Tensor): The flipped image.
  """
  return tf.keras.preprocessing.image.random_shear(image, intensity=intensity)