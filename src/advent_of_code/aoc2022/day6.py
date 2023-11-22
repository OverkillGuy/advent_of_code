"""Day 6 solution to AoC 2022"""

Stream = str
"""The stream of data"""


def detect(stream, window_size: int) -> int:
    """Detect a signal in window_size of a stream

    >>> detect("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4)
    7
    >>> detect("bvwbjplbgvbhsrlpgdmjqwftvncz", 4)
    5
    >>> detect("nppdvjthqldpwncqszvftbrmjlhg", 4)
    6
    >>> detect("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4)
    10
    >>> detect("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4)
    11
    """
    for idx in range(window_size, len(stream) - window_size):
        window = stream[idx - window_size : idx]
        unique_chars_window = set(window)
        # print(f"{idx=},{window=}, {unique_chars_window=}")
        if len(unique_chars_window) == window_size:
            return idx
    raise ValueError("Didn't detect the sequence at all")


def solution1(puzzle_input: str) -> int:
    """Solve day6 part 1"""
    return detect(puzzle_input, 4)


def solution2(puzzle_input: str) -> int:
    """Solve day6 part 2"""
    return detect(puzzle_input, 14)
