#!/usr/bin/python3
"""
Rotate a 2D Matrix by 90 Degrees Clockwise
"""


def rotate_2d_matrix(matrix):
    """Perform a 90-degree clockwise rotation on a
    two-dimensional matrixA two-dimensional list
    representing the matrix
    """
    n = len(matrix)
    i = 0
    j = 0
    while i < int(n / 2):
        y = n - i - 1
        j = i
        while j < y:
            x = n - 1 - j
            # Store the current element in a temporary variable
            tmp = matrix[i][j]
            # Move the top-left element to the top-right position
            matrix[i][j] = matrix[x][i]
            # Move the top-right element to the bottom-right position
            matrix[x][i] = matrix[y][x]
            # Move the bottom-right element to the bottom-left position
            matrix[y][x] = matrix[j][y]
            # Move the bottom-left element to the top-left position
            matrix[j][y] = tmp
            j += 1
        i += 1
