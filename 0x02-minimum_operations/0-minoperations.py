#!/usr/bin/python3
"""
Module for finding the minimum number of operations needed
to result in exactly n 'H' characters.
"""

def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters
    in the file.
    """
    op = 0
    process = 2

    while n > 1:
        if n % process == 0:
            op += process
            n //= process
        else:
            process += 1

    return op
