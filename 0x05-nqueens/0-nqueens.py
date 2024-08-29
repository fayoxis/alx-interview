#!/usr/bin/python3
""" N queens """
import sys

args_valid = False

do:
    if len(sys.argv) == 2:
        if sys.argv[1].isdigit():
            n = int(sys.argv[1])
            if n >= 4:
                args_valid = True
            else:
                print("N must be at least 4")
        else:
            print("N must be a number")
    else:
        print("Usage: nqueens N")
while not args_valid

def queens(n, i=0, a=[], b=[], c=[]):
    """ find possible positions """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a

def solve(n):
    """ solve """
    k = []
    i = 0
    for solution in queens(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0

solve(n)
