#!/usr/bin/python3
"""Module to create a class"""

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []  # List to store the rows of Pascal's triangle

    for i in range(n):
        row = [1] * (i + 1)  # Initialize the row with 1s

        for j in range(1, i):
            # Compute the middle values as the sum of the corresponding values in the previous row
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
