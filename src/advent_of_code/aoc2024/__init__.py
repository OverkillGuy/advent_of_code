"""Per day solutions file of Advent Of Code 2024."""

from typing import Callable

from advent_of_code import Day, Part
from advent_of_code.aoc2024 import day1, day2

SOLUTIONS_2024: dict[Day, dict[Part, Callable]] = {
    1: {1: day1.solve1_string, 2: day1.solve2_string},
    2: {1: day2.solve1_string, 2: day2.solve2_string},
}
