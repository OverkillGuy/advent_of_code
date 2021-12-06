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
        x1, y1, x2, y2 = int(x1s), int(y1s), int(x2s), int(y2s)
        if x1 == x2:  # ignore diagonals: X
            y_low, y_high = min(y1, y2), max(y1, y2)
            grid[x1, y_low : y_high + 1] += 1
        elif y1 == y2:  # ignore diagonals: Y
            x_low, x_high = min(x1, x2), max(x1, x2)
            grid[x_low : x_high + 1, y1] += 1
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
