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

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0

    i = 2
    while True:
        rm_multiples(a, i)
        i += 1
        if i >= len(a):
            break

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None

def rm_multiples(ls, x):
    """removes multiple
    of primes
    """
    i = 2
    do:
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
        i += 1
    while i < len(ls)
