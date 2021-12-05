"""Lookup table for Advent of Code solution functions"""

from typing import Callable, Dict

from advent_of_code_2021.days import day0, day1, day2, day3, day4

SOLUTION_LOOKUP_DAYS: Dict[int, Dict[int, Callable]] = {
    # Dummy day0 with real function to run OK tests
    0: {1: day0.solution1, 2: day0.solution2},
    1: {1: day1.solve1_string, 2: day1.solve2_string},
    2: {1: day2.solve1_stringlist, 2: day2.solve2_stringlist},
    3: {1: day3.solve1_stringlist, 2: day3.solve2_stringlist},
    4: {1: day4.solution1, 2: day4.solution2},
    # Fake day29 with just solution 1, no solution2, for testing
    29: {1: lambda x: 1337},
}
