# mypy: ignore-errors
"""Day5 vents problem, solved via numpy grids"""

import re

import numpy as np
from numpy import typing as npt

line_regex = re.compile("([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)")

# A 2D grid of integers
IntGrid = npt.NDArray[np.uint16]

sample_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def apply_move_lines(grid: IntGrid, x1: int, y1: int, x2: int, y2: int) -> IntGrid:
    """Apply line-moves of (x1,y1) -> (x2,y2) to grid"""
    if x1 == x2:  # ignore diagonals: X
        y_low, y_high = min(y1, y2), max(y1, y2)
        grid[x1, y_low : y_high + 1] += 1
    elif y1 == y2:  # ignore diagonals: Y
        x_low, x_high = min(x1, x2), max(x1, x2)
        grid[x_low : x_high + 1, y1] += 1
    return grid


def solution1(input_str: str, grid_size: int = 10) -> int:
    """Solve day5 problem 1

    >>> solution1(sample_input)
    5
    """
    grid: IntGrid = np.zeros((grid_size,) * 2, dtype=np.uint16)
    matches = line_regex.findall(input_str)
    for x1s, y1s, x2s, y2s in matches:
        # print(f"Move: ({x1s},{y1s}) -> ({x2s},{y2s})")
        # print(format_array(grid))
        grid = apply_move_lines(grid, int(x1s), int(y1s), int(x2s), int(y2s))
    return np.count_nonzero(grid >= 2)


def format_array(grid: IntGrid):
    """Format a grid according to day5 representation"""
    out = ""
    w, h = grid.shape
    for x in range(w):
        for y in range(h):
            cell = grid[y, x]
            if cell != 0:
                out += str(cell)
            else:
                out += "."
        out += "\n"
    return out


def solve1_string(input_str: str):
    """Solve day5 grid with adequate grid size (observed 3 digits)"""
    return solution1(input_str, grid_size=1000)


def apply_move_diag(grid: IntGrid, x1: int, y1: int, x2: int, y2: int) -> IntGrid:
    """Apply line-moves of (x1,y1) -> (x2,y2) to grid"""
    if x1 != x2 and y1 != y2:  # diagonals only
        delta_x = x2 - x1
        dx, dy = np.sign(delta_x), np.sign(y2 - y1)
        # print(f"Move: ({x1},{y1}) -> ({x2},{y2}); {dx=}{dy=}")
        for delta in range(np.abs(delta_x) + 1):
            # print(f"Ticking: ({x1 + dx * delta},{y1 + dy * delta})")
            grid[x1 + dx * delta, y1 + dy * delta] += 1
    return grid


def solution2(input_str: str, grid_size: int = 10) -> int:
    """Solve day5 problem 2

    >>> solution2(sample_input)
    12
    """
    grid: IntGrid = np.zeros((grid_size,) * 2, dtype=np.uint16)
    matches = line_regex.findall(input_str)
    for x1s, y1s, x2s, y2s in matches:
        # print(f"Move: ({x1s},{y1s}) -> ({x2s},{y2s})")
        # print(format_array(grid))
        x1, y1, x2, y2 = int(x1s), int(y1s), int(x2s), int(y2s)
        grid = apply_move_lines(grid, x1, y1, x2, y2)
        grid = apply_move_diag(grid, x1, y1, x2, y2)
    # print(format_array(grid))
    return np.count_nonzero(grid >= 2)


def solve2_string(input_str: str):
    """Solve day5 problem 2 grid with adequate grid size (observed 3 digits)"""
    return solution2(input_str, grid_size=1000)
