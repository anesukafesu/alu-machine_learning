#!/usr/bin/env python3
""" Implements NST
"""
import numpy as np

class NST:
    style_layers = [
        'block1_conv1',
        'bloc2_conv1',
        'block3_conv1',
        'block4_conv1',
        'block5_conv1'
    ]
        
    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        self.__validate_image(style_image, 'style_image')
        self.__validate_image(content_image, 'content_image')

        self.style_image = style_image
        self.content_image = content_image
        self.alpha = alpha
        self.beta = beta
    
    def __validate_alpha_beta(self, value, value_name):
        if value > 0:
            return
        else:
            raise TypeError(
                '{} must be a non-negative number.'.format(value_name)
            )
    
    def __validate_image(self, image, image_name):
        if isinstance(image, np.ndarray) \
            and len(image.shape) == 3 \
            and image.shape[2] == 3:
            return
        else:
            raise TypeError(
                '{} must be a numpy.ndarray with shape (h, w, 3)'.format(image_name)
            )