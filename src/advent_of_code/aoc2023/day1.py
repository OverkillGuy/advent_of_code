"""Day 1 solution to AoC 2023"""

from advent_of_code.input_conversion import to_string_list
from copy import deepcopy

SAMPLE_INPUT = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]

SAMPLE_INPUT2 = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]
CALIBRATION2 = [29, 83, 13,24,42,14,76]


digits = {"one": "1",
          "two": "2",
          "three": "3",
          "four": "4",
          "five": "5",
          "six": "6",
          "seven": "7",
          "eight": "8",
          "nine":"9",
}


def solution1(puzzle_input: list[str]):
    """Solve day1 solution1

    >>> solution1(SAMPLE_INPUT)
    142
    """
    return sum(first_last(line) for line in puzzle_input)

def first_last(line: str):
    """Grab first and last digit of each"""
    digits = [s for s in line if s.isdigit()]
    first, last = digits[0], digits[-1]
    return int(first + last)


def replace(s: str):
    """Replace digits in string form, once"""
    acc = deepcopy(s)
    digits_loc = {acc.find(d):d for d in digits.keys() if acc.find(d) >= 0}
    if not digits_loc:
        return s
    replace_index = min(digits_loc.keys())
    replace_val = digits_loc[replace_index]
    acc = acc.replace(replace_val, digits[replace_val])
    return acc

def recurse_replace(s: str):
    """Replace digits recursively until no more to replace

    >>> all([first_last(recurse_replace(i)) == s for i,s in zip(SAMPLE_INPUT2, CALIBRATION2)])
    True
    """
    prev = ""
    acc = deepcopy(s)
    while acc != prev:
        prev = acc
        acc = replace(acc)
    return acc

def solution2(puzzle_input: list[str]):
    """Solve day1 solution2

    >>> solution2(SAMPLE_INPUT2)
    281
    """
    return solution1([recurse_replace(line) for line in puzzle_input])


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day1 solution1"""
    return solution1(to_string_list(puzzle_input))

def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day1 solution2"""
    return solution2(to_string_list(puzzle_input))
