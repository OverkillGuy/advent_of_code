"""Day 7 solution to AoC 2022"""

import re
from typing import Literal, NamedTuple, Union

FILE_DETAIL_REGEX = re.compile(r"^(\d+|dir|) ([a-z\.]+)$")
"""A single file entry from 'ls' command, or directory"""
COMMAND_REGEX = re.compile(r"""^\$ (ls|cd)\s?([a-z\./]*)$""")
"""A command to execute"""


class CdCommand(NamedTuple):
    """A CD command as tuple"""

    command: Literal["cd"]
    path: str


class LsCommand(NamedTuple):
    """A LS command as tuple"""

    command: Literal["ls"]
    empty: Literal[""]


Commands = Union[CdCommand, LsCommand]

COMMAND_LOOKUP = {"ls": LsCommand, "cd": CdCommand}


class FileDetails(NamedTuple):
    """A file's details as tuple"""

    file_size: int
    file_name: str


class DirDetails(NamedTuple):
    """A directory in LS, as tuple"""

    marker: Literal["dir"]
    dir_name: str


LsOutput = Union[FileDetails, DirDetails]


InputLine = Union[Commands, LsOutput]

# FileSize = int
# """A single file's size"""
# FileSystem = dict[str, Union['FileSystem', FileSize]]
# """A filesystem """

SAMPLE_INPUT_STR = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
SAMPLE_INPUT: list[InputLine] = [
    CdCommand(command="cd", path="/"),
    LsCommand(command="ls", empty=""),
    DirDetails(marker="dir", dir_name="a"),
    FileDetails(file_size=14848514, file_name="b.txt"),
    FileDetails(file_size=8504156, file_name="c.dat"),
    DirDetails(marker="dir", dir_name="d"),
    CdCommand(command="cd", path="a"),
    LsCommand(command="ls", empty=""),
    DirDetails(marker="dir", dir_name="e"),
    FileDetails(file_size=29116, file_name="f"),
    FileDetails(file_size=2557, file_name="g"),
    FileDetails(file_size=62596, file_name="h.lst"),
    CdCommand(command="cd", path="e"),
    LsCommand(command="ls", empty=""),
    FileDetails(file_size=584, file_name="i"),
    CdCommand(command="cd", path=".."),
    CdCommand(command="cd", path=".."),
    CdCommand(command="cd", path="d"),
    LsCommand(command="ls", empty=""),
    FileDetails(file_size=4060174, file_name="j"),
    FileDetails(file_size=8033020, file_name="d.log"),
    FileDetails(file_size=5626152, file_name="d.ext"),
    FileDetails(file_size=7214296, file_name="k"),
]


def solution1(puzzle_input) -> int:
    """Solve day7 part 1"""
    return 0


def solution2(puzzle_input) -> int:
    """Solve day7 part 2"""
    return 0


def parse_input_line(line: str) -> InputLine:
    """Parse a single line of puzzle input

    >>> SAMPLE_INPUT_LINES = SAMPLE_INPUT_STR.splitlines()
    >>> parse_input_line(SAMPLE_INPUT_LINES[0])
    CdCommand(command='cd', path='/')
    >>> parse_input_line(SAMPLE_INPUT_LINES[1])
    LsCommand(command='ls', empty='')
    >>> parse_input_line(SAMPLE_INPUT_LINES[2])
    DirDetails(marker='dir', dir_name='a')
    >>> parse_input_line(SAMPLE_INPUT_LINES[3])
    FileDetails(file_size=14848514, file_name='b.txt')
    >>> parse_input_line(SAMPLE_INPUT_LINES[4])
    FileDetails(file_size=8504156, file_name='c.dat')
    >>> parse_input_line(SAMPLE_INPUT_LINES[5])
    DirDetails(marker='dir', dir_name='d')
    >>> parse_input_line(SAMPLE_INPUT_LINES[6])
    CdCommand(command='cd', path='a')
    >>> parse_input_line(SAMPLE_INPUT_LINES[7])
    LsCommand(command='ls', empty='')
    >>> parse_input_line(SAMPLE_INPUT_LINES[8])
    DirDetails(marker='dir', dir_name='e')
    >>> parse_input_line(SAMPLE_INPUT_LINES[9])
    FileDetails(file_size=29116, file_name='f')
    >>> parse_input_line(SAMPLE_INPUT_LINES[10])
    FileDetails(file_size=2557, file_name='g')
    >>> parse_input_line(SAMPLE_INPUT_LINES[11])
    FileDetails(file_size=62596, file_name='h.lst')
    >>> parse_input_line(SAMPLE_INPUT_LINES[12])
    CdCommand(command='cd', path='e')
    >>> parse_input_line(SAMPLE_INPUT_LINES[13])
    LsCommand(command='ls', empty='')
    >>> parse_input_line(SAMPLE_INPUT_LINES[14])
    FileDetails(file_size=584, file_name='i')
    >>> parse_input_line(SAMPLE_INPUT_LINES[15])
    CdCommand(command='cd', path='..')
    >>> parse_input_line(SAMPLE_INPUT_LINES[16])
    CdCommand(command='cd', path='..')
    >>> parse_input_line(SAMPLE_INPUT_LINES[17])
    CdCommand(command='cd', path='d')
    >>> parse_input_line(SAMPLE_INPUT_LINES[18])
    LsCommand(command='ls', empty='')
    >>> parse_input_line(SAMPLE_INPUT_LINES[19])
    FileDetails(file_size=4060174, file_name='j')
    >>> parse_input_line(SAMPLE_INPUT_LINES[20])
    FileDetails(file_size=8033020, file_name='d.log')
    >>> parse_input_line(SAMPLE_INPUT_LINES[21])
    FileDetails(file_size=5626152, file_name='d.ext')
    >>> parse_input_line(SAMPLE_INPUT_LINES[22])
    FileDetails(file_size=7214296, file_name='k')
    """
    cmd_match = re.fullmatch(COMMAND_REGEX, line)
    if cmd_match:
        return COMMAND_LOOKUP[cmd_match.group(1)](*cmd_match.groups())
    ls_match = re.fullmatch(FILE_DETAIL_REGEX, line)
    if not ls_match:
        raise ValueError("Didn't match any known commands or output")
    if ls_match.group(1).isdigit():
        int_filesize = int(ls_match.group(1))
        return FileDetails(file_size=int_filesize, file_name=ls_match.group(2))
    return DirDetails(marker="dir", dir_name=ls_match.group(2))


def read_puzzle_input(puzzle_input: str) -> list[InputLine]:
    """Process the puzzle input string"""
    return [parse_input_line(line) for line in puzzle_input.splitlines()]


def solve1_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day7 solution1"""
    return solution1(read_puzzle_input(puzzle_input))


def solve2_string(puzzle_input: str) -> int:
    """Convert list to proper format and solve day7 solution2"""
    return solution2(read_puzzle_input(puzzle_input))
