"""Day 3 solution to AoC 2022"""

import string
from functools import cache

Compartment = str
"""The content of a single rucksack compartment, as a string"""
Compartments = tuple[Compartment, Compartment]
"""The two compartments of a rucksack"""

Rucksack = str
"""A single rucksack's content regardless of compartments"""

SAMPLE_INPUT_STR = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

SAMPLE_INPUT: list[Rucksack] = [
    ("vJrwpWtwJgWrhcsFMMfFFhFp"),
    ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"),
    ("PmmdzqPrVvPwwTWBwg"),
    ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"),
    ("ttgJtRGJQctTZtZT"),
    ("CrZsJsPPZsGzwwsLwLmpwMDw"),
]


def split_rucksack_compartments(rucksack: Rucksack) -> Compartments:
    """Split a single rucksack into its two compartment halves"""
    half = len(rucksack) // 2
    return rucksack[:half], rucksack[half:]


def only_common_item(rucksack: Rucksack) -> str:
    """Return the only item in sack common between compartments

    >>> only_common_item("vJrwpWtwJgWrhcsFMMfFFhFp")
    'p'
    >>> only_common_item("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
    'L'
    >>> only_common_item("PmmdzqPrVvPwwTWBwg")
    'P'
    """
    compartments = split_rucksack_compartments(rucksack)
    first, second = compartments
    set_intersection = set(list(first)) & set(list(second))
    # Problem definition guarantees only one char intersection
    return set_intersection.pop()


@cache
def char_priority(char: str) -> int:
    """Compute the priority of a character

    >>> char_priority("a"), char_priority("b"), char_priority("z")
    (1, 2, 26)
    >>> char_priority("A"), char_priority("B"), char_priority("Z")
    (27, 28, 52)
    """
    if char not in string.ascii_letters:
        raise ValueError(f"Character priority only works on chars; Was given '{char}'")
    ascii_value_lower_a = ord("a")
    PRIORITY_LOOKUP: dict[str, int] = {}
    for char_lower in string.ascii_lowercase:
        ascii_value_char = ord(char_lower)
        ascii_offset = ascii_value_char - ascii_value_lower_a
        PRIORITY_LOOKUP[char_lower] = ascii_offset + 1
    ascii_value_upper_a = ord("A")
    for char_upper in string.ascii_uppercase:
        ascii_value_char = ord(char_upper)
        ascii_offset = ascii_value_char - ascii_value_upper_a
        PRIORITY_LOOKUP[char_upper] = ascii_offset + 26 + 1
    return PRIORITY_LOOKUP[char]


def solution1(puzzle_input: list[Rucksack]) -> int:
    """Solve day3 part 1

    >>> solution1(SAMPLE_INPUT)
    157
    """
    acc = 0
    for rucksack in puzzle_input:
        intersection_char = only_common_item(rucksack)
        acc += char_priority(intersection_char)
    return acc


def solution2(puzzle_input) -> int:
    """Solve day3 part 2"""
    return 0


def read_puzzle_input(puzzle_input: str) -> list[Rucksack]:
    r"""Process the puzzle input string

    >>> read_puzzle_input("vJrwpWtwJgWrhcsFMMfFFhFp\n")
    ['vJrwpWtwJgWrhcsFMMfFFhFp']
    >>> read_puzzle_input(SAMPLE_INPUT_STR) == SAMPLE_INPUT
    True
    """
    return puzzle_input.splitlines()


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day3 solution1"""
    return solution1(read_puzzle_input(puzzle_input))


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day3 solution2"""
    return solution2(read_puzzle_input(puzzle_input))
