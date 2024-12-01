"""Day 1 solution to AoC 2023"""

from advent_of_code.input_conversion import to_string_list

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
CALIBRATION2 = [29, 83, 13, 24, 42, 14, 76]


digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def first_last(line: str):
    """Grab first and last digit of each"""
    digits = [s for s in line if s.isdigit()]
    first, last = digits[0], digits[-1]
    return int(first + last)


def solution1(puzzle_input: list[str]):
    """Solve day1 solution1

    >>> solution1(SAMPLE_INPUT)
    142
    """
    return sum(first_last(line) for line in puzzle_input)


def filter_digits(s: str):
    """Replace and filter digits, even if in string form (part 2)

    Note the crucial check here: overlaps are allowed:

    >>> filter_digits("eighthree")
    83
    >>> filter_digits("sevenine")
    79

    And cross-checking the given solutions:

    >>> all([filter_digits(i) == s for i,s in zip(SAMPLE_INPUT2, CALIBRATION2)])
    True
    """
    acc = []
    for index, char in enumerate(s):
        if char.isdigit():
            acc.append(char)
        for digit_s, digit_i in digits.items():
            # This char spells a digit: add it too (but no modifying s!)
            if s[index:].find(digit_s) == 0:
                acc.append(digit_i)
    first, last = acc[0], acc[-1]
    return int(first + last)


def solution2(puzzle_input: list[str]):
    """Solve day1 solution2

    >>> solution2(SAMPLE_INPUT2)
    281
    """
    return sum(filter_digits(line) for line in puzzle_input)


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day1 solution1"""
    return solution1(to_string_list(puzzle_input))


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day1 solution2"""
    return solution2(to_string_list(puzzle_input))
