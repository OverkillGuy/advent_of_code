"""Day 2 solution to AoC 2023"""
from typing import Literal, TypeAlias

"""First, we state the Puzzle Input objects, as given.
Note these may be terrible to use for solving, but perfect to represent the inputs."""
GameID: TypeAlias = int
"""A single game's ID"""
Color: TypeAlias = Literal["red", "blue", "green"]
"""The potential colors of cubs"""
Grab: TypeAlias = dict[Color, int]
"""A single grab in the bag = how many of each color was revealed"""
Game: TypeAlias = tuple[GameID, list[Grab]]
"""A single game = sequence of multiple grabs"""
Games: TypeAlias = list[Game]
"""A record of multiple games"""


def solution1(puzzle_input) -> int:
    """Solve day2 part 1"""
    return 0


def solution2(puzzle_input) -> int:
    """Solve day2 part 2"""
    return 0


def read_puzzle_input(puzzle_input: str):
    """Process the puzzle input string"""
    return puzzle_input


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day2 solution1"""
    return solution1(read_puzzle_input(puzzle_input))


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day2 solution2"""
    return solution2(read_puzzle_input(puzzle_input))
