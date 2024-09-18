#!/usr/bin/python3

""" this will Make Change in the Algorithm """


def makeChange(coins, total):
    """ Calculates the minimum number of coins needed to
    make the given total value. coins (list): A list of coin
    denominations. total (int): The target value to be made with coins.
    Returns: int: The minimum number of coins needed to make
    the target value. If the target value cannot be made with
    the given coins, returns -1.
    If the target value is 0 or less, returns 0.
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0

    change = 0
    coins = sorted(coins, reverse=True)
    i = 0

    while total > 0:
        if i >= len(coins):
            return -1
        coin = coins[i]
        while total >= coin:
            total -= coin
            change += 1
        i += 1

    return change
