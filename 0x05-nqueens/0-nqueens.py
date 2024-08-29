#!/usr/bin/python3
""" N queens """
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

n = int(sys.argv[1])

if n < 4:
    print("N must be at least 4")
    exit(1)

def queens(n, i=0, a=[], b=[], c=[]):
    """ find possible positions """
    solutions = []
    
    def backtrack():
        nonlocal i, a, b, c
        if i == n:
            solutions.append(a[:])
        else:
            j = 0
            while True:
                if j not in a and i + j not in b and i - j not in c:
                    a.append(j)
                    b.append(i + j)
                    c.append(i - j)
                    i += 1
                    backtrack()
                    i -= 1
                    a.pop()
                    b.pop()
                    c.pop()
                j += 1
                if j >= n:
                    break

    backtrack()
    return solutions

def solve(n):
    """ solve """
    solutions = queens(n)
    
    for solution in solutions:
        k = [[i, s] for i, s in enumerate(solution)]
        print(k)

solve(n)
