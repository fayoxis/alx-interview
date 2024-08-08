#!/usr/bin/python3
"""
Module for finding the minimum number of operations needed
to result in exactly n 'H' characters.
"""


def min_operations(n):
    """
    Calculates the fewest number of operations
    """
    if n < 2:
        return 0

    operations = 0
    root = 2

    while root <= n:
        if n % root == 0:
            operations += root
            n //= root
            root -= 1
        root += 1

    return operations
