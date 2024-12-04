"""Day 4 solution to AoC 2024"""

import re

import numpy as np

XMAS_REGEX = re.compile("XMAS")


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
        acc += count
    return acc


def generate_diagonals(array):
    """Generate the diagonal strings from a given array"""
    min_size = len("XMAS")
    width = array.shape[0] - min_size
    w_low, w_high = (
        -width,
        width + 1,
    )  # range stops at end - 1, so offset by one to include
    height = array.shape[1] - min_size
    h_low, h_high = -height, height + 1
    diags = [
        "".join(np.diagonal(array, offset=i).tolist()) for i in range(w_low, w_high)
    ]
    diags_reverse = [line[::-1] for line in diags]
    flipped = np.flip(array, axis=0)
    diags_flip = [
        "".join(np.diagonal(flipped, offset=i).tolist()) for i in range(h_low, h_high)
    ]
    diags_flip_reverse = [line[::-1] for line in diags_flip]
    return [diags, diags_reverse, diags_flip, diags_flip_reverse]


def generate_flips(arr) -> list[list[str]]:
    """Generate the flipped versions of the input"""
    horizontal = ["".join(list(arr[i, :])) for i in range(arr.shape[0])]
    h_reverse = [line[::-1] for line in horizontal]
    vertical = ["".join(list(arr[:, i])) for i in range(arr.shape[1])]
    v_reverse = [line[::-1] for line in vertical]
    return [horizontal, h_reverse, vertical, v_reverse]


def solution1(puzzle_input) -> int:
    """Solve day4 part 1

    >>> solution1(SAMPLE_INPUT)
    18
    """
    acc = 0
    arr = np.array([list(line) for line in puzzle_input.splitlines()])
    variants = generate_flips(arr) + generate_diagonals(arr)
    for variant_index, lines in enumerate(variants):
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
