#!/usr/bin/python3
"""Island Perimeter Problem
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid
    Args:
        grid: 2d list of integers containing 0(water) or 1(land)
    Return:
        the perimeter of the island
    """

    p = 0
    i = 0
    j = 0

    do:
        if (grid[i][j] == 1):
            if (i <= 0 or grid[i - 1][j] == 0):
                p += 1
            if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                p += 1
            if (j <= 0 or grid[i][j - 1] == 0):
                p += 1
            if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                p += 1

        j += 1
        if j >= len(grid[i]):
            j = 0
            i += 1

    while i < len(grid)

    return p
