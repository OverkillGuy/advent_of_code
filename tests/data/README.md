# Advent of code test inputs

This folder contains my personal test inputs, by year, for test purposes.

The per-day doctests only go so far to "prove" the solution given is correct, so
throwing realistic problem data agaisnt the proposed solution is the only way to
confirm validity.

To that end, I've collected my personal inputs from advent of code in order to
run the actual solutions I collect through actual known-good input, and its
known-good answers.

### Where's the test?

See `/tests/test_aoc.py` for the logic that tests using this folder

### What's up with days 0 and 29?

Obviously, there is no day 0 or day 29 in [advent of
code](https://adventofcode.com), but I found helpful when writing the CLI runner
script (see `/features/aoc_runner.feature` for a description of the CLI feature)
to keep a couple dummy solutions to confirm the CLI feature against.

The further round of testing that this data folder enables is perfect to assess
the solutions I provide by iterating over what the CLI can read, and that does
include the dummy day 0 and 29.
