"""Day 3, binary things"""

from typing import List


def digit_list_to_int(digits: List[int]) -> int:
    """Transform a list of binary digits into the base 10 integer it represents

    >>> digit_list_to_int([1, 0, 1, 1, 0])
    22
    >>> digit_list_to_int([0, 1, 0, 0, 1])
    9
    """
    digits_as_string = "".join([str(i) for i in digits])
    return int(digits_as_string, 2)


def count_one_digits(input_list: List[str]) -> List[int]:
    """Count the number of digits set to one per number

    >>> count_one_digits(['011', '101', '111'])
    [2, 2, 3]
    >>> count_one_digits(["011110111110", "110111000111"])
    [1, 2, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1]
    """
    digit_one_counts = [0] * len(input_list[0])
    for number in input_list:
        for digit_index, digit in enumerate(list(number)):
            digit_one_counts[digit_index] += int(digit)
    return digit_one_counts


def most_common_digits(input_list: List[str]) -> List[int]:
    """Find most common value of digit in a list

    >>> most_common_digits(["00100", "11110", "10110", "10111", "10101", "01111"])
    [1, 0, 1, 1, 1]
    >>> most_common_digits(["011", "001"])
    [0, 1, 1]
    """
    digit_one_counts = count_one_digits(input_list)
    half_of_input = len(input_list) // 2
    return [
        1 if digit_one_count >= half_of_input else 0
        for digit_one_count in digit_one_counts
    ]


def solution1(input_list: List[str]) -> int:
    r"""Solve day3 problem 1

    >>> solution1(["00100", "11110", "10110", "10111", "10101", "01111", "00111",
    ...            "11100", "10000", "11001", "00010", "01010"])
    198
    >>> solution1(["00100\n", "11110\n", "10110\n", "10111", "10101", "01111", "00111",
    ...            "11100", "10000", "11001", "00010", "01010"])
    198
    """
    numbers_list = [number_str.strip() for number_str in input_list]
    gamma_digits = most_common_digits(numbers_list)
    # Epsilon digits are opposite of (gamma_digit)
    epsilon_digits = [
        1 if digit_one_count == 0 else 0 for digit_one_count in gamma_digits
    ]
    gamma, epsilon = digit_list_to_int(gamma_digits), digit_list_to_int(epsilon_digits)
    return gamma * epsilon
