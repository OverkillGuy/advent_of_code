"""Day 3 solution to AoC 2024"""

import re

SAMPLE_INPUT_STR = (
    """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
)

MUL_REGEX = re.compile(r"mul\(([0-9]+)+,([0-9]+)\)")


def solution1(puzzle_input: str) -> int:
    """Solve day3 part 1

    >>> solution1(SAMPLE_INPUT_STR)
    161
    """
    acc = 0
    matches = MUL_REGEX.findall(puzzle_input)
    for left, right in matches:
        acc += int(left) * int(right)
    return acc


def solution2(puzzle_input: str) -> int:
    """Solve day3 part 2"""
    return 0


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day3 solution1"""
    return solution1(puzzle_input)


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day3 solution2"""
    return solution2(puzzle_input)
