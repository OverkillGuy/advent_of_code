Feature: Advent of code solution runner
  As a Advent of code developer
  I need a CLI to select which solution to run given day and input
  So that I show per-user result on request


Scenario: AOC CLI without args shows help
  Given the installed CLI
  When I invoke "poetry run aoc --help"
  Then the exit code is OK
  And output contains help
