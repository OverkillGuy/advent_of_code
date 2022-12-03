"""Day 3 solution to AoC 2022"""

Compartment = str
"""The content of a single rucksack compartment, as a string"""
Rucksack = tuple[Compartment, Compartment]
"""A single rucksack's content, compartment by compartment"""

SAMPLE_INPUT_STR = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

SAMPLE_INPUT: list[Rucksack] = [
    ("vJrwpWtwJgWr", "hcsFMMfFFhFp"),
    ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"),
    ("PmmdzqPrV", "vPwwTWBwg"),
    ("wMqvLMZHhHMvwLH", "jbvcjnnSBnvTQFn"),
    ("ttgJtRGJ", "QctTZtZT"),
    ("CrZsJsPPZsGz", "wwsLwLmpwMDw"),
]


def solution3(puzzle_input) -> int:
    """Solve day3 part 1"""
    return 0


def solution2(puzzle_input) -> int:
    """Solve day3 part 2"""
    return 0


def read_puzzle_input(puzzle_input: str) -> list[Rucksack]:
    r"""Process the puzzle input string

    >>> read_puzzle_input("vJrwpWtwJgWrhcsFMMfFFhFp\n")
    [('vJrwpWtwJgWr', 'hcsFMMfFFhFp')]
    >>> read_puzzle_input(SAMPLE_INPUT_STR) == SAMPLE_INPUT
    True
    """
    acc = []
    for line in puzzle_input.splitlines():
        half = len(line) // 2
        acc.append((line[:half], line[half:]))
    return acc


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day3 solution1"""
    return solution2(read_puzzle_input(puzzle_input))


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day3 solution2"""
    return solution2(read_puzzle_input(puzzle_input))
