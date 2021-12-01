Feature: Advent of code solution runner
  As a Advent of code developer
  I need a CLI to select which solution to run given day and input
  So that I show per-user result on request


Scenario: AOC CLI without args shows help
  Given the installed CLI
  When I invoke "poetry run aoc --help"
  Then the exit code is OK
  And output contains help

Scenario: CLI solve runs OK on mock-day 0
  Given a dummy input file
  When I invoke "poetry run aoc --day 0 --input-file dummy.txt"
  Then the exit code is OK
  And output gives number "10"


Scenario: CLI solution 2 runs OK on mock-day 0
  Given a dummy input file
  When I invoke "poetry run aoc --solution2 --day 0 --input-file dummy.txt"
  Then the exit code is OK
  And output gives number "20"


Scenario: Asking for a day without solution fails
  Given a dummy input file
  When I invoke "poetry run aoc --day 30 --input-file dummy.txt"
  Then the exit code is nonzero
  And output is an error

Scenario: Asking for a day's problem2 without solution2 fails
  Given a dummy input file
  When I invoke "poetry run aoc --solution2 --day 29 --input-file dummy.txt"
  Then the exit code is nonzero
  And output is an error
