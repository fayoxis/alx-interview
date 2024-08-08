#!/usr/bin/python3
"""
Module for finding the minimum number of operations needed
to result in exactly n 'H' characters.
"""


def calculate_min_operations(n: int) -> int:
    """
    Computes the minimum number of operations required
    to obtain exactly n 'H' characters in the file.
    """
    operations = 0
    current_process = 2

    while n > 1:
        while n % current_process == 0:
            operations += current_process
            n //= current_process

        current_process += 1

    return operations
