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
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                for case in switch(i, j, grid):
                    if case(0, 0): # top-left corner
                        p += 2
                        break
                    if case(0, -1): # top edge
                        p += 1
                        break
                    if case(-1, 0): # left edge
                        p += 1
                        break
                    if case(-1, -1): # general case
                        if (i <= 0 or grid[i - 1][j] == 0):
                            p += 1
                        if (j <= 0 or grid[i][j - 1] == 0):
                            p += 1
                        if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                            p += 1
                        if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                            p += 1
                        break
    return p

def switch(i, j, grid):
    cases = {
        (0, 0): lambda: i == 0 and j == 0,
        (0, -1): lambda: i == 0 and j > 0,
        (-1, 0): lambda: i > 0 and j == 0,
        (-1, -1): lambda: True
    }
    return cases.values()
