Feature: Validate the solution via real input files
  As a developer solving Advent of Code
  I need to validate my solutions work with real input data from personal input
  So that my answer are plausible

# The actual combo of [year + day + part] is given
# by /src/advent_of_code/solutions_lookup.py
# which is used also by the CLI

Scenario Outline: Proving each solved day works on real input
  Given an input file for day <day number> of <year number>
  And the known solution for day <day number> part <part number>
  When I run the solution with input file of day <day number> of <year number>
  Then the answer is an integer
  And the answer is equal to the known solution
