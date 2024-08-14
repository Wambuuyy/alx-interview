#!/usr/bin/env python3
"""Rotate a nxn 2d matrix 90 degrees clockwise"""

def rotate_2d_matrix(matrix):
    """
    to do in place operations(swapping, reverse) to avoid using space
    1. **Transpose the Matrix**: 
       - In the transposition step, we convert rows into columns.
       - Specifically, for each element at position (i, j) in the matrix, 
         we swap it with the element at position (j, i). 
       - This operation is done only for elements above the diagonal (where i < j) 
         to avoid redundant swaps.
       - The diagonal elements remain unchanged, as swapping them would not change their positions.

    2. **Reverse Each Row**:
       - After transposing the matrix, we reverse the order of elements in each row.
       - This final step completes the 90-degree clockwise rotation.

    matrix = [1 2 3]
             [4 5 6]
             [7 8 9]
    transposition = [1 4 7]
                    [2 5 8]
                    [3 6 9]
    reverse = [7 4 1]
              [8 5 2]
              [9 6 3]
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
