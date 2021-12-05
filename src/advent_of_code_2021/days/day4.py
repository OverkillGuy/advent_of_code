"""Day4, a bingo game"""

import re
from typing import List

W, H = 5, 5
num_regex = "([0-9]{2}| [0-9])"
line_regex = " ".join([num_regex] * W)
grid_regex = re.compile("\n".join([line_regex] * H))


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


def parse_grids(input_str: str) -> List[List[int]]:
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
