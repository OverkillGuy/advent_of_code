"""Day 2 solution to AoC 2023"""
import re
from typing import Literal, TypeAlias

from advent_of_code.input_conversion import to_string_list

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


GAMES_SPLIT_REGEX = re.compile("^Game (\d+): (.+)$")
"""Splits game into id + grabs"""

COLORS_REGEX = "|".join(Color.__args__)  # type: ignore[attr-defined]
"""The Color literal, as regex for {py:const}`GRAB_SPLIT_REGEX`"""
GRAB_SPLIT_REGEX = re.compile(f"(\d+) ({COLORS_REGEX})")
"""How to split a single grab into color pairs"""

REFERENCE_BAG: Grab = {"red": 12, "green": 13, "blue": 14}
"""The reference bag we're supposed to check against"""


def solution1(puzzle_input) -> int:
    """Solve day2 part 1"""
    return 0


def is_possible(to_check: Game, ref: Grab) -> bool:
    """Checks that the Game to_check matches ref bag contents

    Checks using the info given: "games 1, 2, and 5 would have been possible"...

    >>> is_possible(SAMPLE_INPUT[0], REFERENCE_BAG)
    True
    >>> is_possible(SAMPLE_INPUT[1], REFERENCE_BAG)
    True
    >>> is_possible(SAMPLE_INPUT[2], REFERENCE_BAG)
    False
    >>> is_possible(SAMPLE_INPUT[3], REFERENCE_BAG)
    False
    >>> is_possible(SAMPLE_INPUT[4], REFERENCE_BAG)
    True
    """
    return True


def solution2(puzzle_input) -> int:
    """Solve day2 part 2"""
    return 0


def read_puzzle_input(puzzle_input: str) -> Games:
    """Process the puzzle input string

    >>> read_puzzle_input(SAMPLE_INPUT_STR) == SAMPLE_INPUT
    True
    """
    acc: Games = []
    for line in to_string_list(puzzle_input):
        matches = GAMES_SPLIT_REGEX.match(line)
        if matches is None:
            raise ValueError(f"Bad game line: '{line}'")
        game_id, game_str = matches.groups()
        grab_lst = [grab.strip() for grab in game_str.split(";")]
        grabs: list[Grab] = []
        for grab in grab_lst:
            grab_matches = GRAB_SPLIT_REGEX.findall(grab)
            grab_obj: Grab = {}
            for num, color in grab_matches:
                grab_obj[color] = int(num)
            grabs.append(grab_obj)
        acc.append((int(game_id), grabs))
    return acc


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day2 solution1"""
    return solution1(read_puzzle_input(puzzle_input))


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day2 solution2"""
    return solution2(read_puzzle_input(puzzle_input))
