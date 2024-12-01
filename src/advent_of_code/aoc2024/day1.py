"""Day 1 solution to AoC 2024"""

from collections import Counter

Location = int
LocationList = list[Location]
PuzzleInput = tuple[LocationList, LocationList]


SAMPLE_INPUT_STR = """3   4
4   3
2   5
1   3
3   9
3   3"""
SAMPLE_INPUT: PuzzleInput = ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])


def solution1(puzzle_input: PuzzleInput) -> int:
    """Solve day1 part 1

    >>> solution1(SAMPLE_INPUT)
    11
    """
    left_list, right_list = puzzle_input
    sorted_left, sorted_right = sorted(left_list), sorted(right_list)
    return sum([abs(left - right) for left, right in zip(sorted_left, sorted_right)])


def solution2(puzzle_input: PuzzleInput) -> int:
    """Solve day1 part 2

    >>> solution2(SAMPLE_INPUT)
    31
    """
    left_list, right_list = puzzle_input
    right_counter = Counter(right_list)
    sum = 0
    for left_digit in left_list:
        right_occurences = right_counter.get(left_digit, 0)
        sum += left_digit * right_occurences
    return sum


def read_puzzle_input(puzzle_input: str) -> PuzzleInput:
    """Process the puzzle input string

    >>> read_puzzle_input(SAMPLE_INPUT_STR)
    ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])
    """
    lines = puzzle_input.splitlines()
    grid = [line.split("   ") for line in lines]
    return [int(left) for left, right in grid], [int(right) for left, right in grid]


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day1 solution1"""
    return solution1(read_puzzle_input(puzzle_input))


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day1 solution2"""
    return solution2(read_puzzle_input(puzzle_input))
