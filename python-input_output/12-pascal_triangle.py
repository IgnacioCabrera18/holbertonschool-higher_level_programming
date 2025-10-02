#!/usr/bin/python3

"""Module pascal_triangle"""


def pascal_triangle(n):
    """Function pascal_triangle"""
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        act_row = [1] * (1 + i)
        if i > 1:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                act_row[j] = prev_row[j - 1] + prev_row[j]
        triangle.append(act_row)
    return triangle
