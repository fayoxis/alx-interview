#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""

def isWinner(x, nums):
    """x - rounds
    nums - numbers list
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    max_num = max(nums)
    a = [1] * (max_num + 1)
    a[0] = a[1] = 0

    i = 2
    while i < len(a):
        j = 2 * i
        while j < len(a):
            a[j] = 0
            j += i
        i += 1

    for num in nums:
        if sum(a[:num + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None
