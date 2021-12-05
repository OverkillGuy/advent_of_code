"""Day4, a bingo game"""

import re
from typing import List, Tuple

import numpy as np
from numpy import typing as npt

W, H = 5, 5

NumbersDrawn = List[int]
Grid = List[int]
Grids = List[Grid]


# A 2D grid of integers
NumpyGrid = npt.NDArray[np.uint8]
# A 2D grid of booleans
CheckGrid = npt.NDArray[np.bool_]
# Aggregate of bool+int grid, for playing a round
NpGrid = Tuple[NumpyGrid, CheckGrid]


num_regex = "([0-9]{2}| [0-9])"
line_regex = " ".join([num_regex] * W)
grid_regex = re.compile("\n".join([line_regex] * H))

# Sample grids for doctest purposes
# Defined here because harder to do in doctest (line too long)
single_grid_str = """50 79 88 34  0
56 46  5 17 31
29  6 38 78 68
75 57 15 44 83
89 45 43 85 72"""

multi_grid_str = """29  8 56 15 33
 7 14 51 88 67
91 32 62 18 73
53 63 49 34 46
70 25 77 87 31

38 92 26 65 77
59 39  4 57 16
91 45 35 36  2
34 40 89  8 62
96 28 31 88 33

93 96 73 40 13
57 59 88 32 78
48 72 23 42 62
41  7 85 84 44
95 91 52 61  8"""

simple_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


def parse_grids(input_str: str) -> Grids:
    r"""Read grids from string, returning array of grid-array

    >>> grids = parse_grids(single_grid_str)
    >>> len(grids), len(grids[0])
    (1, 25)
    >>> type(grids[0][0]) == int
    True
    >>> multigrid = parse_grids(multi_grid_str)
    >>> len(multigrid), len(multigrid[0])
    (3, 25)
    >>> type(multigrid[0][0]) == int
    True
    """
    grid_matches = grid_regex.findall(input_str)
    grids: List[List[int]] = []
    for grid_found in grid_matches:
        grid = [int(i) for i in grid_found]
        grids.append(grid)
    return grids


def parse_input(input_str: str) -> Tuple[NumbersDrawn, Grids]:
    """Parse puzzle input into understandable objects

    >>> drawn, grids = parse_input(simple_input)
    >>> len(drawn), type(drawn[0])
    (27, <class 'int'>)
    >>> len(grids), len(grids[0])
    (3, 25)
    """
    strings_list = input_str.split("\n")
    first_string, rest_string = strings_list[0], strings_list[1:]
    drawn_list = [int(i) for i in first_string.split(",")]
    grids = parse_grids("\n".join(rest_string))
    return drawn_list, grids


def grid_list_to_np_grid(grid: Grid) -> NpGrid:
    """Reform grid in both numpy array of int, and np array of boolean at False

    >>> grid = parse_grids(single_grid_str)[0]
    >>> int_grid, bool_grid = grid_list_to_np_grid(grid)
    >>> type(int_grid), type(bool_grid)
    (<class 'numpy.ndarray'>, <class 'numpy.ndarray'>)
    >>> int_grid.dtype, bool_grid.dtype
    (dtype('uint8'), dtype('bool'))
    >>> int_grid.shape == bool_grid.shape == (5, 5)
    True
    """
    np_grid = np.array(grid, dtype=np.uint8).reshape(W, H)
    return (np_grid, np.zeros_like(np_grid, dtype=bool))
