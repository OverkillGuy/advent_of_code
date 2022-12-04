"""Day 4 solution to AoC 2022"""

import re

SectorID = int

Assignment = tuple[SectorID, SectorID]
"""A single elf's assignment"""
Pair = tuple[Assignment, Assignment]
"""A pair of assignments"""

PAIRS_REGEX = re.compile(r"^(\d+)-(\d+),(\d+)-(\d+)$")
"""Regex defining a pair of assignment aka puzzle input line"""

SAMPLE_INPUT_STR = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

SAMPLE_INPUT: list[Pair] = [
    ((2, 4), (6, 8)),
    ((2, 3), (4, 5)),
    ((5, 7), (7, 9)),
    ((2, 8), (3, 7)),
    ((6, 6), (4, 6)),
    ((2, 6), (4, 8)),
]


def solution1(puzzle_input) -> int:
    """Solve day4 part 1"""
    return 0


def solution2(puzzle_input) -> int:
    """Solve day4 part 2"""
    return 0


def read_puzzle_input(puzzle_input: str) -> list[Pair]:
    """
    Process the puzzle input string

    >>> read_puzzle_input(SAMPLE_INPUT_STR) == SAMPLE_INPUT
    True
    """
    acc = []
    for line in puzzle_input.splitlines():
        match = re.match(PAIRS_REGEX, line)
        if not match:
            raise ValueError(f"Line didn't follow puzzle input regex: '{line}'")
        pair: Pair = (
            (int(match.group(1)), int(match.group(2))),
            (int(match.group(3)), int(match.group(4))),
        )
        acc.append(pair)
    return acc


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day4 solution1"""
    return solution1(read_puzzle_input(puzzle_input))


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day4 solution2"""
    return solution2(read_puzzle_input(puzzle_input))
