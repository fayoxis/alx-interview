#!/usr/bin/python3
"""
Module for finding the minimum number of operations needed
to result in exactly n 'H' characters.
"""


def minOperations(n: int) -> int:
    """calculates the fewest number of operations
    needed to result in exactly n H characters
    in the file"""
    process = 2
    op = 0
    while True:
        op_count = 0
        do {
            if n % process == 0:
                op_count += process
                n //= process
            else:
                break
        } while (True)
        if op_count == 0:
            break
        op += op_count
        process += 1
    return op
