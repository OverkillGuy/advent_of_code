"""Day 1 solution to AoC 2024"""

SAMPLE_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3"""

Location = int
LocationList = list[Location]
PuzzleInput = tuple[LocationList, LocationList]


def solution1(puzzle_input: PuzzleInput) -> int:
    """Solve day1 part 1"""
    return 0


def solution2(puzzle_input: PuzzleInput) -> int:
    """Solve day1 part 2"""
    return 0


def read_puzzle_input(puzzle_input: str) -> PuzzleInput:
    """Process the puzzle input string

    >>> read_puzzle_input(SAMPLE_INPUT)
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
