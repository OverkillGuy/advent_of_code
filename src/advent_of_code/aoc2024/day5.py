"""Day 5 solution to AoC 2024"""

from collections import defaultdict

PrevDict = dict[int, set[int]]
Update = list[int]
UpdateList = list[Update]
Day5Input = tuple[PrevDict, UpdateList]

SAMPLE_INPUT_STR = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

SAMPLE_INPUT_PREV: PrevDict = {
    47: {53, 13, 61, 29},
    97: {13, 61, 47, 29, 53, 75},
    75: {29, 53, 47, 61, 13},
    61: {13, 53, 29},
    29: {13},
    53: {29, 13},
}
SAMPLE_INPUT_UPDATES: UpdateList = [
    [75, 47, 61, 53, 29],
    [97, 61, 53, 29, 13],
    [75, 29, 13],
    [75, 97, 47, 61, 53],
    [61, 13, 29],
    [97, 13, 75, 29, 47],
]

SAMPLE_INPUT: Day5Input = (SAMPLE_INPUT_PREV, SAMPLE_INPUT_UPDATES)


def solution1(puzzle_input) -> int:
    """Solve day5 part 1"""
    return 0


def solution2(puzzle_input) -> int:
    """Solve day5 part 2"""
    return 0


def read_puzzle_input(puzzle_input: str) -> Day5Input:
    """Process the puzzle input string

    >>> read_puzzle_input(SAMPLE_INPUT_STR) == SAMPLE_INPUT
    True
    """
    lines = puzzle_input.splitlines()
    index_split = lines.index("")
    dict_lines, update_lines = lines[:index_split], lines[index_split + 1 :]
    prevs: PrevDict = defaultdict(set)
    updates: UpdateList = []
    for dict_line in dict_lines:
        before, after = dict_line.split("|")
        prevs[int(before)] = prevs[int(before)] | {int(after)}
    for update_line in update_lines:
        updates.append([int(i) for i in update_line.split(",")])
    return prevs, updates


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day5 solution1"""
    return solution1(read_puzzle_input(puzzle_input))


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day5 solution2"""
    return solution2(read_puzzle_input(puzzle_input))
