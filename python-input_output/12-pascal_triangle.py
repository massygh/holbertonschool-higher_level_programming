#!/usr/bin/python3
"""Module to create a class"""

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []  # List to store the rows of Pascal's triangle

    for i in range(n):
        row = []  # List to store the values of the current row

        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)  # The first and last values of each row are always 1
            else:
                # Compute the middle values as the sum of the corresponding values in the previous row
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        triangle.append(row)

    return triangle
