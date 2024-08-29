#!/usr/bin/python3
""" N queens """
import sys

if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)

n = int(sys.argv[1])

def queens(n, i=0, a=[], b=[], c=[]):
    """ find possible positions """
    positions = []
    while i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                new_a = a + [j]
                new_b = b + [i + j]
                new_c = c + [i - j]
                positions.extend(queens(n, i + 1, new_a, new_b, new_c))
        break
    if i == n:
        positions.append(a)
    return positions

def solve(n):
    """ solve """
    k = []
    i = 0
    solutions = queens(n, 0)
    while solutions:
        solution = solutions.pop(0)
        while solution:
            s = solution.pop(0)
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0

solve(n)
