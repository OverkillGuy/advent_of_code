"""Day 5 solution to AoC 2022"""

Crate = str
"""A single crate (single character string)"""

Stack = list[Crate]
"""A single stack of crate = vertical slice, bottom to top (last item = top)"""

Stacks = list[Stack]
"""The entirety of the stacks used as problem input, last is rightmost"""

Movement = tuple[int, int, int]
"""A planned movement of [1] crates from stack [2] to stack [3]"""

Problem = tuple[Stacks, list[Movement]]
"""The problem as given"""

SAMPLE_INPUT_STR = """
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

SAMPLE_INPUT: Problem = (
    [["Z", "N"], ["M", "C", "D"], ["P"]],
    [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)],
)


def solution1(puzzle_input) -> int:
    """Solve day5 part 1"""
    return 0


def solution2(puzzle_input) -> int:
    """Solve day5 part 2"""
    return 0


def read_puzzle_input(puzzle_input: str) -> Problem:
    """Process the puzzle input string"""
    return ([], [])


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day5 solution1"""
    return solution1(read_puzzle_input(puzzle_input))


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day5 solution2"""
    return solution2(read_puzzle_input(puzzle_input))
