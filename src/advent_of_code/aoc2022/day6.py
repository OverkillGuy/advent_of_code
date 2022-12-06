"""Day 6 solution to AoC 2022"""

Stream = str
"""The stream of data"""


def solution1(puzzle_input, window_size=4) -> int:
    """Solve day6 part 1

    >>> solution1("mjqjpqmgbljsphdztnvjfqwrcgsmlb")
    7
    >>> solution1("bvwbjplbgvbhsrlpgdmjqwftvncz")
    5
    >>> solution1("nppdvjthqldpwncqszvftbrmjlhg")
    6
    >>> solution1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
    10
    >>> solution1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
    11
    """
    for idx in range(window_size, len(puzzle_input) - window_size):
        window = puzzle_input[idx - window_size : idx]
        unique_chars_window = set(window)
        # print(f"{idx=},{window=}, {unique_chars_window=}")
        if len(unique_chars_window) == window_size:
            return idx
    raise ValueError("Didn't detect the sequence at all")


def solution2(puzzle_input) -> int:
    """Solve day6 part 2"""
    return 0


def solve1_string(puzzle_input: Stream) -> int:
    """Convert list to proper format and solve day6 solution1"""
    return solution1(puzzle_input)


def solve2_string(puzzle_input: Stream) -> int:
    """Convert list to proper format and solve day6 solution2"""
    return solution2(puzzle_input)
