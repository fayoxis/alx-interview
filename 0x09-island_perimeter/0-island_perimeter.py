#!/usr/bin/python3
""" Island Perimeter Problem This program calculates
the perimeter of an island represented in a 2D grid.
"""

def island_perimeter(grid):
    """ Calculate the perimeter of the island in the given grid (list):
    A 2D list of integers, where 0 represents water and 1
    represents land. int: The perimeter of the island.
    """

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):  # If the current cell is land
                for case in switch(i, j, grid):
                    if case(0, 0):  # Top-left corner case
                        perimeter += 2
                        break
                    if case(0, -1):  # Top edge case
                        perimeter += 1
                        break
                    if case(-1, 0):  # Left edge case
                        perimeter += 1
                        break
                    if case(-1, -1):  # General case
                        # Check if the current cell is surrounded by water on each side
                        if (i <= 0 or grid[i - 1][j] == 0):
                            perimeter += 1
                        if (j <= 0 or grid[i][j - 1] == 0):
                            perimeter += 1
                        if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                            perimeter += 1
                        if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                            perimeter += 1
                        break
    return perimeter

def switch(i, j, grid):
    """ Define cases for different positions of the current cell
    in the grid. dict_values: A set of lambda functions
    representing different cases.
    """
    cases = {
        (0, 0): lambda: i == 0 and j == 0,  # Top-left corner
        (0, -1): lambda: i == 0 and j > 0,  # Top edge
        (-1, 0): lambda: i > 0 and j == 0,  # Left edge
        (-1, -1): lambda: True  # General case
    }
    return cases.values()
