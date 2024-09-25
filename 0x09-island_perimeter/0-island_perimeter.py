#!/usr/bin/python3
"""Island Perimeter Problem"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid
    Args:
        grid: 2d list of integers containing 0(water) or 1(land)
    Return:
        the perimeter of the island
    """

    p = 0
    i, j = 0, 0
    rows, cols = len(grid), len(grid[0])

    while i < rows:
        while j < cols:
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    p += 1
                if i == rows - 1 or grid[i + 1][j] == 0:
                    p += 1
                if j == 0 or grid[i][j - 1] == 0:
                    p += 1
                if j == cols - 1 or grid[i][j + 1] == 0:
                    p += 1
            j += 1
        i += 1
        j = 0

    return p
