"""Day 2 solution to AoC 2024"""

Level = int
Report = list[Level]
PuzzleInput = list[Report]

SAMPLE_INPUT_STR = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

SAMPLE_INPUT: PuzzleInput = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]


def is_safe(report: Report) -> bool:
    """Computes if a report is safe

    >>> is_safe(SAMPLE_INPUT[0])
    True
    >>> is_safe(SAMPLE_INPUT[-1])
    True
    >>> [is_safe(i) for i in SAMPLE_INPUT[1:-1]]
    [False, False, False, False]
    """
    diffs = [n0 - n1 for n0, n1 in zip(report[:-1], report[1:])]
    diff_is_negative = [diff < 0 for diff in diffs]
    if not all(diff == diff_is_negative[0] for diff in diff_is_negative[1:]):
        return False
    return all(1 <= abs(diff) <= 3 for diff in diffs)


def solution1(puzzle_input: PuzzleInput) -> int:
    """Solve day2 part 1"""
    return 0


def solution2(puzzle_input) -> int:
    """Solve day2 part 2"""
    return 0


def read_puzzle_input(puzzle_input: str) -> PuzzleInput:
    """Process the puzzle input string

    >>> read_puzzle_input(SAMPLE_INPUT_STR) == SAMPLE_INPUT
    True
    """
    return [[int(num) for num in line.split()] for line in puzzle_input.splitlines()]


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day2 solution1"""
    return solution1(read_puzzle_input(puzzle_input))


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day2 solution2"""
    return solution2(read_puzzle_input(puzzle_input))
