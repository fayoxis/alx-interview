#!/usr/bin/python3
"""
Module for finding the minimum number of operations needed
to result in exactly n 'H' characters.
"""


def minOperations(n: int) -> int:
    """calculates  number of operations
    """
    process = 2
    op = 0
    if n > 1:
        if n % process == 0:
            op += process
            n /= process
        process += 1
    return op
