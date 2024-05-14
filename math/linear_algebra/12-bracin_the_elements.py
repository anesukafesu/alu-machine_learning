#!/usr/bin/env python3
import numpy as np


def np_elementwise(mat1, mat2):
    sum = mat1 + mat2
    difference = mat1 - mat2
    product = mat1 * mat2
    quotient = mat1 / mat2

    return sum, difference, product, quotient
