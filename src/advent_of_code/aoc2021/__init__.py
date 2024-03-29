"""Per day solutions file of Advent Of Code 2021."""

from typing import Callable

from advent_of_code import Day, Part
from advent_of_code.aoc2021 import day0, day1, day2, day3, day4, day5, day6, day7

SOLUTIONS_2021: dict[Day, dict[Part, Callable]] = {
    # Dummy day0 with real function to run OK tests
    0: {1: day0.solution1, 2: day0.solution2},
    1: {1: day1.solve1_string, 2: day1.solve2_string},
    2: {1: day2.solve1_stringlist, 2: day2.solve2_stringlist},
    3: {1: day3.solve1_stringlist, 2: day3.solve2_stringlist},
    4: {1: day4.solution1, 2: day4.solution2},
    5: {1: day5.solve1_string, 2: day5.solve2_string},
    6: {1: day6.solution1, 2: day6.solution2},
    7: {1: day7.solution1, 2: day7.solution2},
    # Fake day29 with just solution 1, no solution2, for testing
    29: {1: lambda x: 1337},
}
