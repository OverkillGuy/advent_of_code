"""Day 3 solution to AoC 2024"""

import re

Start = int
End = int
Range = tuple[Start, End]
IsDo = bool

SAMPLE_INPUT_STR = (
    """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
)
SAMPLE_INPUT_STR2 = (
    """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
)

MUL_REGEX = re.compile(r"mul\(([0-9]+),([0-9]+)\)")
DODONT_REGEX = re.compile(r"(don't|do)\(\)")


def solution1(puzzle_input: str) -> int:
    """Solve day3 part 1

    >>> solution1(SAMPLE_INPUT_STR)
    161
    """
    acc = 0
    matches = MUL_REGEX.findall(puzzle_input)
    for left, right in matches:
        acc += int(left) * int(right)
    return acc


def solution2(puzzle_input: str) -> int:
    """Solve day3 part 2

    >>> solution2(SAMPLE_INPUT_STR2)
    48
    """
    delims: list[tuple[Range, IsDo]] = []
    for delim_match in DODONT_REGEX.finditer(puzzle_input):
        range = delim_match.span()
        is_do = delim_match.group(1) == "do"
        delims.append((range, is_do))
    puzzle_cut = ""
    cursor = 0
    active = True
    for (start, end), do in delims:
        if do and active:
            continue
        if not do and not active:
            continue
        if do:  # not active yet: active + move cursor
            active = True
            cursor = end
        if not do:  # It's a DONT = STOP READING, copy text
            puzzle_cut += puzzle_input[cursor:start]
            cursor = end
            active = False
    # Deal with end of string
    if cursor != len(puzzle_input) and active:
        puzzle_cut += puzzle_input[cursor:]
    return solution1(puzzle_cut)


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day3 solution1"""
    return solution1(puzzle_input)


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day3 solution2"""
    return solution2(puzzle_input)
