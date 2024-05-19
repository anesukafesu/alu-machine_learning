#!/usr/bin/env python3
""" Implements the cat_matrices method
"""


def cat_matrices(mat1, mat2, axis=0):
    """Function to recursively concatenate matrices along the specified axis
    """
    def recursive_concat(mat1, mat2, axis):
        if isinstance(mat1, list) and isinstance(mat2, list):
            if len(mat1) != len(mat2):
                return None
            if axis == 0:
                return [recursive_concat(mat1[i], mat2[i], axis) for i in range(len(mat1))]
            elif axis == 1:
                return [mat1[i] + mat2[i] for i in range(len(mat1))]
            else:
                return None
        elif isinstance(mat1, (int, float)) and isinstance(mat2, (int, float)):
            return mat1 + mat2
        else:
            return None

    # Check if the dimensions along the specified axis are compatible
    if axis >= len(mat1) or axis >= len(mat2):
        return None

    # Check if dimensions are compatible for concatenation
    if axis == 0:
        if len(mat1) != len(mat2):
            return None
    elif axis == 1:
        if len(mat1[0]) != len(mat2[0]):
            return None

    # Concatenate matrices recursively
    return recursive_concat(mat1, mat2, axis)

# Example usage:
mat1 = [[[1, 2], [3, 4]],
        [[5, 6], [7, 8]]]

mat2 = [[[9, 10], [11, 12]],
        [[13, 14], [15, 16]]]

result = cat_matrices(mat1, mat2, axis=0)
if result is not None:
    print("Concatenated matrix along axis 0:")
    for layer in result:
        for row in layer:
            print(row)
        print()
else:
    print("Cannot concatenate matrices along the specified axis.")

result = cat_matrices(mat1, mat2, axis=1)
if result is not None:
    print("\nConcatenated matrix along axis 1:")
    for layer in result:
        for row in layer:
            print(row)
        print()
else:
    print("Cannot concatenate matrices along the specified axis.")
