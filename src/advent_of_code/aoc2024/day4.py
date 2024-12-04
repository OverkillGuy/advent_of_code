"""Day 4 solution to AoC 2024"""

import re

import numpy as np

XMAS_REGEX = re.compile("XMAS")

SAMPLE_INPUT1 = """....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX"""


SAMPLE_INPUT = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


def count_xmas(lines: list[str]) -> int:
    """Count the number of XMAS in given lines"""
    acc = 0
    for line in lines:
        count = len(XMAS_REGEX.findall(line))
        print(f"{line=}{count=}")
        acc += count
    return acc


def generate_diagonals(array):
    """Generate the diagonal strings from a given array"""
    min_size = len("XMAS")
    width = array.shape[0] - min_size
    low, high = -width, +width
    diags = ["".join(np.diagonal(array, offset=i).tolist()) for i in range(low, high)]
    diags_reverse = [
        "".join(np.diagonal(array, offset=i).tolist()[::-1]) for i in range(low, high)
    ]
    flipped = np.flip(array)
    diags_flip = [
        "".join(np.diagonal(flipped, offset=i).tolist()) for i in range(low, high)
    ]
    diags_flip_reverse = [
        "".join(np.diagonal(flipped, offset=i).tolist()[::-1]) for i in range(low, high)
    ]
    return [diags, diags_reverse, diags_flip, diags_flip_reverse]


def generate_flips(arr) -> list[list[str]]:
    """Generate the flipped versions of the input"""
    horizontal = ["".join(list(arr[i, :])) for i in range(arr.shape[0])]
    h_reverse = ["".join(list(arr[i, :])[::-1]) for i in range(arr.shape[0])]
    vertical = ["".join(list(arr[:, i])) for i in range(arr.shape[1])]
    v_reverse = ["".join(list(arr[:, i])[::-1]) for i in range(arr.shape[1])]
    return [horizontal, h_reverse, vertical, v_reverse]


def solution1(puzzle_input) -> int:
    """Solve day4 part 1

    >>> solution1(SAMPLE_INPUT1)
    18
    """
    acc = 0
    arr = np.array([list(line) for line in puzzle_input.splitlines()])
    variants = generate_flips(arr) + generate_diagonals(arr)
    for lines in variants:
        acc += count_xmas(lines)
    return acc


def solution2(puzzle_input) -> int:
    """Solve day4 part 2"""
    return 0


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day4 solution1"""
    return solution1(puzzle_input)


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day4 solution2"""
    return solution2(puzzle_input)
