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

SAMPLE_INPUT_STR = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

SAMPLE_INPUT: Games = [
    (1, [{"blue": 3, "red": 4}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}]),
    (
        2,
        [
            {"blue": 1, "green": 2},
            {"green": 3, "blue": 4, "red": 1},
            {"green": 1, "blue": 1},
        ],
    ),
    (
        3,
        [
            {"green": 8, "blue": 6, "red": 20},
            {"blue": 5, "red": 4, "green": 13},
            {"green": 5, "red": 1},
        ],
    ),
    (
        4,
        [
            {"green": 1, "red": 3, "blue": 6},
            {"green": 3, "red": 6},
            {"green": 3, "blue": 15, "red": 14},
        ],
    ),
    (5, [{"red": 6, "blue": 1, "green": 3}, {"blue": 2, "red": 1, "green": 2}]),
]


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
