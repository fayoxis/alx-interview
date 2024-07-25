#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.
    
    Args:
    n (int): Number of rows to generate.
    
    Returns:
    list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []
    
    triangle = []
    
    for row in range(n):
        current_row = [1] * (row + 1)
        
        for j in range(1, row):
            current_row[j] = triangle[row-1][j-1] + triangle[row-1][j]
        
        triangle.append(current_row)
    
    return triangle
