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


def subsets(pair: Pair) -> bool:
    """Is an assignment the subset of the other in the pair?

    Solved via set anchor intersection.

    Note it's also possible to solve this via range-set-equality if we allocate memory:

        set(range(first_start,first_end)) == set(range(second_start, second_end))

    BUT memory grows linearly based on:

        O(max(first_end - first_start, second_end - second_start))
        ~ O(M-N)
        ~ O(N) on range size

    which means OOM/DoS for ranges like (1, 10e99999). Anchor-comparison is
    O(1) in memory for the same M,N.

    >>> [subsets(pair) for pair in SAMPLE_INPUT]
    [False, False, False, True, True, False]

    """
    first, second = pair
    (first_start, first_end), (second_start, second_end) = first, second
    # Disjoint sets (no shared item)
    if first_start > second_end or second_start > first_end:
        return False  # Disjoint cannot be subset
    # Since sets not disjoint, any shared anchor = one is subset
    if first_start == second_start or first_end == second_end:
        return True
    # Sets are subset if either range's is both start_anchor_min and end_anchor_max
    # Noting that this min/max fails for == case, but we ensured no equality already
    # So we can do strict integer comparison to get unambiguous min/max
    first_start_is_min: bool = first_start > second_start
    first_end_is_max: bool = first_end < second_end
    # We don't care which one is subset, just that one IS subset
    return first_start_is_min == first_end_is_max


def solution1(puzzle_input: list[Pair]) -> int:
    """
    Solve day4 part 1

    >>> solution1(SAMPLE_INPUT)
    2
    """
    return sum(subsets(pair) for pair in puzzle_input)


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
