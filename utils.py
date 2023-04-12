#!/usr/bin/env python3
"""utilties module for Conway gof"""


def checker(matrix, i, j):
    """
    Checks the value of the cells surrounding the current target cell
    including the diagonals.
    Args:
        matrix (): the matrix use to implement the game of life cell.
        i (): the row index of the target cell.
        j (): the column index of the target cell.

    Returns:
        The total number of neighbors.

    """
    neighbors = 0
    if i != 0:
        try:
            if j != 0:
                neighbors += 1 if matrix[i - 1][j - 1] == 1 else 0
            neighbors += 1 if matrix[i - 1][j] == 1 else 0
            neighbors += 1 if matrix[i - 1][j + 1] == 1 else 0
        except IndexError:
            pass
    try:
        if j != 0:
            neighbors += 1 if matrix[i][j - 1] == 1 else 0
        neighbors += 1 if matrix[i][j + 1] == 1 else 0
    except IndexError:
        pass
    if i != len(matrix) - 1:
        try:
            if j != 0:
                neighbors += 1 if matrix[i + 1][j - 1] == 1 else 0
            neighbors += 1 if matrix[i + 1][j] == 1 else 0
            neighbors += 1 if matrix[i + 1][j + 1] == 1 else 0
        except IndexError:
            pass
    return neighbors


def new_grid(old_grid, size):
    """
    Takes in a matrix and set is cells on or off base on the following rules.

    Rules:
        1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        2. Any live cell with two or three live neighbours lives on to the next generation.
        3. Any live cell with more than three live neighbours dies, as if by overpopulation.
        4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

    Args:
        old_grid ([n][n]): matrix with the state of all the cells.
        size (int): size of the matrix.

    Returns:
        A new matrix  with the new state of all cells.

    """
    new_grid = [[0 for _ in range(size * 2)] for _ in range(size)]

    for i, val in enumerate(old_grid):
        for j, _ in enumerate(val):
            # dies as if of underpopulation or overpopulation

            check = checker(old_grid, i, j)
            if (check < 2 or check > 3) and old_grid[i][j] == 1:
                new_grid[i][j] = 0
            # survive as having 2 to 3 neighbors
            if (check == 3 or check == 2) and old_grid[i][j] == 1:
                new_grid[i][j] = 1
            # Comes back to life as if by reproduction
            if check == 3 and old_grid[i][j] == 0:
                new_grid[i][j] = 1

    return new_grid  #
#
# def set_block(grid):
#     try:
#         grid[2][1] = 1
#         grid[2][2] = 1
#         grid[3][1] = 1
#         grid[1][1] = 1
#     except IndexError:
#         pass
#
#
# def print_matrix(matrix):
#     for i in matrix:
#         for j in i:
#             print(f"{j} ", end=" ")
#         print()
