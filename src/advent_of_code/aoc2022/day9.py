"""Day 9 solution to AoC 2022"""

import re



from scipy.sparse import csr_array

from scipy.sparse.csgraph import dijkstra

import numpy as np


PATH_REGEX = re.compile(r"""(\w+) to (\w+) = (\d+)""")
"""A path from X to Y and the distance"""

Location = str
"""A single location to travel to/from"""

Distance = int
"""Measure of how distant things are"""

AdjacencyDict = dict[Location, list[Location]]
"""A record of how key is adjacent to values"""

Adjacency = tuple[Location, Location, Distance]

DistanceLookup = dict[Location, Distance]
"""How far is Location from source, as Distance"""

SAMPLE_INPUT_STR = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""

SAMPLE_INPUT: list[Adjacency] = [
    ("London", "Dublin", 464),
    ("London", "Belfast", 518),
    ("Dublin", "Belfast", 141),
]


def solution1(puzzle_input: list[Adjacency]) -> int:
    """Solve day9 part 1"""
    adjacency_matrix_size = len(puzzle_input)
    graph = csr_array([adjacency_matrix_size]*2, dtype=np.uint8)
    for src, dest, distance in puzzle_input:
        graph[src, dest] = distance
    dist_matrix, predecessors = dijkstra(csgraph=graph, directed=True, indices=0, return_predecessors=False)
    return 0


def solution2(puzzle_input) -> int:
    """Solve day9 part 2"""
    return 0

def read_puzzle_input(puzzle_input: str) -> list[Adjacency]:
    """
    Process the puzzle input string

    >>> read_puzzle_input(SAMPLE_INPUT_STR) == SAMPLE_INPUT
    True
    """
    acc = []
    for line in puzzle_input.splitlines():
        match = re.fullmatch(PATH_REGEX, line)
        if not match:
            raise ValueError(f"Puzzle line mismatches: {line}")
        src, dest, distance = match.group(1), match.group(2), int(match.group(3))
        acc.append((src, dest, distance))
    return acc

def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day9 solution1"""
    return solution1(read_puzzle_input(puzzle_input))


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day9 solution2"""
    return solution2(read_puzzle_input(puzzle_input))
