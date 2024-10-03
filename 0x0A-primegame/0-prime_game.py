#!/usr/bin/python3
"""Prime Game playing a game where they take turns
choosing different numbers from a set of consecutive
integers. The game ends when there are no more
numbers left to choose. The player who picks
the last remaining prime number wins the game."""


def isWinner(x, nums):
    """ Determines the winner of the Prime Game.
    rounds (int): The number of rounds in the game.
    (list): The list of consecutive int to choose from. 
    str: The name of the winner ("Ben" or "Maria"),
    or None if there is no winner
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
