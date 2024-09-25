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

    p = 0  # Initialize the perimeter counter
    i = 0  # Initialize the row index
    j = 0  # Initialize the column index

    do:
        # Check if the current cell is land (1)
        if (grid[i][j] == 1):
            # Check if the cell above is out of bounds or is water
            if (i <= 0 or grid[i - 1][j] == 0):
                p += 1  # Increment the perimeter

            # Check if the cell below is out of bounds or is water
            if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                p += 1  # Increment the perimeter

            # Check if the cell to the left is out of bounds or is water
            if (j <= 0 or grid[i][j - 1] == 0):
                p += 1  # Increment the perimeter

            # Check if the cell to the right is out of bounds or is water
            if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                p += 1  # Increment the perimeter

        # Move to the next column
        j += 1

        # If we've reached the end of the current row
        if j >= len(grid[i]):
            # Reset the column index to 0
            j = 0
            # Move to the next row
            i += 1

    # Continue the loop until we've checked all rows
    while i < len(grid)

    return p  # Return the calculated perimeter
