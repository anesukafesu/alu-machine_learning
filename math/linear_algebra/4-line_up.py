#!/usr/bin/env python3


def add_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return None
    
    result = []

    for num1, num2 in zip(arr1, arr2):
        result.append(num1 + num2)
    
    return result
