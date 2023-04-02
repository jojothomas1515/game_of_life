#!/usr/bin/env python3



def checker(matrix, i, j):
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


def new_grid(old_grid, n):
    new_grid = [[0 for _ in range(n)] for _ in range(n)]

    for i, val in enumerate(old_grid):
        for j, _ in enumerate(val):
            # dies as if of underpopulation or overpopulation

            if (checker(old_grid, i, j) < 2 or
                checker(old_grid, i, j) > 3) and \
                    old_grid[i][j] == 1:
                new_grid[i][j] = 0
            # survive as having 2 to 3 neighbors
            if (checker(old_grid, i, j) == 3 or
                checker(old_grid, i, j) == 2) and \
                    old_grid[i][j] == 1:
                new_grid[i][j] = 1
            # Comes back to life as if by reproduction
            if checker(old_grid, i, j) == 3 and old_grid[i][j] == 0:
                new_grid[i][j] = 1

    # for i, vali in enumerate(new_grid):
    #     for j, vj in enumerate(vali):
    #         old_grid[i][j] = vj

    return new_grid

def set_block(grid):
    try:
        grid[2][1]= 1
        grid[2][2]= 1
        grid[3][1]= 1
        grid[1][1]= 1
    except IndexError:
        pass

def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(f"{j} ", end=" ")
        print()

