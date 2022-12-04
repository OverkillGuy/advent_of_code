"""Day 3 solution to AoC 2022"""

import string
from functools import cache

Compartment = str
"""The content of a single rucksack compartment, as a string"""
Compartments = tuple[Compartment, Compartment]
"""The two compartments of a rucksack"""

Rucksack = str
"""A single rucksack's content regardless of compartments"""

ElfGroup = tuple[Rucksack, Rucksack, Rucksack]
"""Backpacks of an elf group"""

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


def common_item_compartment(rucksack: Rucksack) -> str:
    """Return the only item in sack common between compartments

    >>> common_item_compartment("vJrwpWtwJgWrhcsFMMfFFhFp")
    'p'
    >>> common_item_compartment("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
    'L'
    >>> common_item_compartment("PmmdzqPrVvPwwTWBwg")
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
        intersection_char = common_item_compartment(rucksack)
        acc += char_priority(intersection_char)
    return acc


def group_badge(elf_group: ElfGroup) -> str:
    """Return the badge of an elf group, only item common between all three Rucksacks

    >>> group_badge(SAMPLE_INPUT[:3])
    'r'
    >>> group_badge(SAMPLE_INPUT[3:])
    'Z'
    """
    first, second, third = elf_group
    set_intersection = set(list(first)) & set(list(second)) & set(list(third))
    # Problem definition guarantees only one char intersection
    return set_intersection.pop()


def solution2(puzzle_input: list[Rucksack]) -> int:
    """
    Solve day3 part 2

    >>> solution2(SAMPLE_INPUT)
    70
    """
    # Group 3 by 3 by iterating over same list offset by 1 & 2
    acc = 0
    elves = puzzle_input
    for elf_group in zip(elves[::3], elves[1::3], elves[2::3]):
        badge = group_badge(elf_group)
        acc += char_priority(badge)
    return acc


def read_puzzle_input(puzzle_input: str) -> list[Rucksack]:
    r"""
    Process the puzzle input string

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
