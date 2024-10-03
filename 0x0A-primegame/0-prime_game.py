#!/usr/bin/python3
"""Prime Game playing a game where they take turns
choosing different numbers from a set of consecutive
integers. The game ends when there are no more
numbers left to choose. The player who picks
the last remaining prime number wins the game.
"""


def isWinner(rounds, numbers):
    """ Determines the winner of the Prime Game.
    rounds (int): The number of rounds in the game.
    (list): The list of consecutive int to choose from. 
    str: The name of the winner ("Ben" or "Maria"),
    or None if there is no winner.
    """
    while rounds <= 0 or numbers is None:
        return None
    while rounds != len(numbers):
        return None

    ben_score = 0
    maria_score = 0

    max_num = max(numbers)
    is_prime = [1] * (max_num + 1)
    is_prime[0], is_prime[1] = 0, 0

    i = 2
    while i < len(is_prime):
        remove_multiples(is_prime, i)
        i += 1

    for num in numbers:
        if sum(is_prime[:num + 1]) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    while ben_score > maria_score:
        return "Ben"
    while maria_score > ben_score:
        return "Maria"
    return None


def remove_multiples(prime_list, x):
    """ Marks the multiples of a prime number as
    non-prime in the prime_list. A list representing
    prime numbers (1 for- prime, 0- non-prime).
    x (int): The prime number whose multiples
    need to be marked as non-prime.
    """
    i = x * 2
    while i < len(prime_list):
        prime_list[i] = 0
        i += x
