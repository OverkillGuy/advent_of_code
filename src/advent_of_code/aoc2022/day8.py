"""Day 8 solution to AoC 2022"""

from enum import Enum

TreeElevation = int
Row = list[TreeElevation]
Grid = list[Row]


SAMPLE_INPUT_STR = """30373
25512
65332
33549
35390
"""
SAMPLE_INPUT: Grid = [
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0],
]


class Direction(Enum):
    """Cardinal directions as numbers"""

    UP = 0
    RIGHT = 1
    LEFT = 2
    DOWN = 3


def solution1(puzzle_input: Grid) -> int:
    """Solve day8 part 1"""
    return count_visibility(puzzle_input)


def solution2(puzzle_input) -> int:
    """Solve day8 part 2"""
    return 0


def column(grid: Grid, column_index: int) -> Row:
    """Grab column of a grid at given index"""
    return [row[column_index] for row in grid]


def is_visible(tree: TreeElevation, sightline: Row) -> bool:
    """Compute if a given tree's evelation is visible, given LOS (distance ASC start=1)

    >>> is_visible(5, [2]), is_visible(5, [0])
    (True, True)
    >>> is_visible(5, SAMPLE_INPUT[1][2:]), is_visible(5, column(SAMPLE_INPUT, 2)[3:])
    (False, False)
    >>> is_visible(5, [3]), is_visible(5, SAMPLE_INPUT[1][3:])
    (True, True)
    >>> is_visible(5, SAMPLE_INPUT[1][:2]), is_visible(5, column(SAMPLE_INPUT,2)[2:])
    (False, False)
    >>> is_visible(5, [])
    True
    """
    return all(tree > item for item in sightline)


def line_of_sight(
    grid: Grid, tree_row: int, tree_column: int, direction: Direction
) -> Row:
    """Compute the line of sight in a given direction"""
    if direction == Direction.UP:
        return column(grid, tree_column)[:tree_row]
    if direction == Direction.DOWN:
        return column(grid, tree_column)[tree_row + 1 :]
    if direction == Direction.LEFT:
        return grid[tree_row][:tree_column]
    if direction == Direction.RIGHT:
        return grid[tree_row][tree_column + 1 :]
    raise ValueError("Incorrect direction")


def count_visibility(grid: Grid) -> int:
    """Count how many trees in the grid are visible

    >>> count_visibility(SAMPLE_INPUT)
    21
    """
    acc = 0
    for row_index, row in enumerate(grid):
        for column_index, tree_height in enumerate(row):
            tree_visible = False
            for direction in Direction:
                if tree_visible:
                    continue  # no point checking, it's visible already
                sightline = line_of_sight(grid, row_index, column_index, direction)
                if is_visible(tree_height, sightline):
                    tree_visible = True
                    continue
            acc += tree_visible * 1
    return acc


def read_puzzle_input(puzzle_input: str) -> Grid:
    """Process the puzzle input string

    >>> read_puzzle_input(SAMPLE_INPUT_STR) == SAMPLE_INPUT
    True
    """
    return [[int(i) for i in line.strip()] for line in puzzle_input.splitlines()]


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day8 solution1"""
    return solution1(read_puzzle_input(puzzle_input))


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day8 solution2"""
    return solution2(read_puzzle_input(puzzle_input))
