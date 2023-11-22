"""Day 5 solution to AoC 2022"""

import re
from copy import deepcopy
from typing import NamedTuple

Crate = str
"""A single crate (single character string)"""

Stack = list[Crate]
"""A single stack of crate = vertical slice, bottom to top (last item = top)"""

Stacks = list[Stack]
"""The entirety of the stacks used as problem input, last is rightmost"""


class Movement(NamedTuple):
    """A planned movement of [1] crates from stack [2] to stack [3]"""

    quantity: int
    src: int
    dest: int


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
    [Movement(1, 2, 1), Movement(3, 1, 3), Movement(2, 2, 1), Movement(1, 1, 2)],
)

MOVE_REGEX = re.compile(r"^move (\d+) from (\d+) to (\d+)$")
"""Regex matching a single line of intended movement in the puzzle input"""


def apply_move(stacks: Stacks, move: Movement) -> Stacks:
    """Apply a single movement to the stack"""
    moved: list[Crate] = []
    for _ in range(move.quantity):  # As many times as needed
        moved.append(stacks[move.src - 1].pop())  # Push the popped value
    stacks[move.dest - 1].extend(moved)
    return stacks


def apply_move_retainorder(stacks: Stacks, move: Movement) -> Stacks:
    """Apply a single movement to the stack, retaining order per part 2

    >>> apply_move_retainorder([["Z","N","D"],["M", "C"],["P"]], SAMPLE_INPUT[1][1])
    [[], ['M', 'C'], ['P', 'Z', 'N', 'D']]

    >>> apply_move_retainorder([[], ['M', 'C'], ['P', 'Z', 'N', 'D']], SAMPLE_INPUT[1][2])
    [['M', 'C'], [], ['P', 'Z', 'N', 'D']]
    """
    moved: list[Crate] = []
    for _ in range(move.quantity):  # As many times as needed
        moved.append(stacks[move.src - 1].pop())  # Push the popped value
    stacks[move.dest - 1].extend(moved[::-1])
    return stacks


def solution1(puzzle_input: Problem) -> str:
    """Solve day5 part 1

    >>> solution1(SAMPLE_INPUT)
    'CMZ'
    """
    stacks, moves = deepcopy(puzzle_input)
    for move in moves:
        stacks = apply_move(stacks, move)
    return "".join([s.pop() for s in stacks])


def solution2(puzzle_input: Problem) -> str:
    """Solve day5 part 2

    >>> solution2(SAMPLE_INPUT)
    'MCD'
    """
    stacks, moves = deepcopy(puzzle_input)
    for move in moves:
        stacks = apply_move_retainorder(stacks, move)
    return "".join([s.pop() for s in stacks])


def parse_move(move_line: str) -> Movement:
    """Parse a single line of movement"""
    matches = re.match(MOVE_REGEX, move_line)
    if not matches:
        raise ValueError(f"Bad line given for move parsing: {move_line}")
    return Movement(int(matches.group(1)), int(matches.group(2)), int(matches.group(3)))


def read_puzzle_input(puzzle_input: str) -> Problem:
    """Process the puzzle input string

    >>> read_puzzle_input(SAMPLE_INPUT_STR) == SAMPLE_INPUT
    True
    """
    stacks: dict[int, Stack] = {}
    moves: list[Movement] = []
    reading_moves = False  # We start by reading stack
    for line in puzzle_input.splitlines():
        if not line:
            continue  # Skip empty lines, nothing to parse
        if reading_moves:  # Read moves not stack
            moves.append(parse_move(line))
            continue
        # Reading stack: Check for stack separator
        if line[1].isdigit():
            reading_moves = True
            continue
        # Reading stack
        # Input in reverse order (bottom at end), will reverse on complete
        # Slicing works because we assume single-char stack name
        stack_slice = line[1::4]  # Read every 4th char starting offset by 1
        for stack_idx, stack_char in enumerate(stack_slice):
            if stack_idx not in stacks:
                stacks[stack_idx] = []  # Populate empty stack list
            if stack_char.strip():  # Non-empty = something there
                stacks[stack_idx].append(stack_char)
    # Reverse the stacks to get top = last item, for stack.pop()
    stacks_sorted_by_idx = [stacks[idx][::-1] for idx in sorted(stacks.keys())]
    return (stacks_sorted_by_idx, moves)


def solve1_string(puzzle_input: str) -> str:
    """Convert list to proper format and solve day5 solution1"""
    return solution1(read_puzzle_input(puzzle_input))


def solve2_string(puzzle_input: str) -> str:
    """Convert list to proper format and solve day5 solution2"""
    return solution2(read_puzzle_input(puzzle_input))
