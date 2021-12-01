"""CLI dispatcher to run a specific day's solutions"""

import argparse
import sys


def parse_arguments(arguments):
    """Parse generic arguments, given as parameters"""
    parser = argparse.ArgumentParser("aoc", description="Advent of Code runner 2021")
    parser.add_argument("-d", "--day", type=int, help="What day's problem to solve")
    parser.add_argument(
        "-f",
        "--input-file",
        type=argparse.FileType("r"),
        help="Input file for that day",
    )
    return parser.parse_args(arguments)


def cli():
    """Run the aoc cli"""
    _ = parse_arguments(sys.argv[1:])
    pass
