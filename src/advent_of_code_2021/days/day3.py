"""Day 3, binary things"""

from typing import List, Optional

from advent_of_code_2021.input_conversion import to_string_list


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
    """Find most common value of digit in a list, biased to 1 on equality

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


def most_common_digits_balanced(input_list: List[str]) -> List[Optional[int]]:
    """Find most common value of digit in a list, None if equality

    >>> most_common_digits_balanced(["0010", "1110", "1010", "1011", "1011", "0111"])
    [1, 0, 1, None]
    >>> most_common_digits_balanced(["011", "001"])
    [0, None, 1]
    """
    digit_one_counts = count_one_digits(input_list)
    half_of_input = len(input_list) / 2
    results: List[Optional[int]] = []
    for digit_one_count in digit_one_counts:
        if digit_one_count == half_of_input:
            results.append(None)
        elif digit_one_count > half_of_input:
            results.append(1)
        else:
            results.append(0)
    return results


def binary_not_digit_list(input_list: List[int]) -> List[int]:
    """Inverse a binary number's values

    >>> binary_not_digit_list([0, 1 , 1])
    [1, 0, 0]
    """
    return [1 if digit == 0 else 0 for digit in input_list]


def binary_not_digit_list_noneable(
    input_list: List[Optional[int]],
) -> List[Optional[int]]:
    """Inverse a binary number's values, passing None through as-is

    >>> binary_not_digit_list_noneable([0, 1, None])
    [1, 0, None]
    """
    return [None if bit is None else 1 if bit == 0 else 0 for bit in input_list]


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
    # Epsilon digits are opposite of gamma_digit
    epsilon_digits = binary_not_digit_list(gamma_digits)
    gamma, epsilon = digit_list_to_int(gamma_digits), digit_list_to_int(epsilon_digits)
    return gamma * epsilon


def bit_criteria(input_list: List[str], use_most_common_digit: bool = True) -> int:
    """Compute the bit criteria per part 2

    >>> bit_criteria(["00100", "11110", "10110", "10111", "10101", "01111", "00111",
    ...               "11100", "10000", "11001", "00010", "01010"],
    ...               use_most_common_digit=True)
    23
    >>> bit_criteria(["00100", "11110", "10110", "10111", "10101", "01111", "00111",
    ...               "11100", "10000", "11001", "00010", "01010"],
    ...               use_most_common_digit=False)
    10
    """
    number_bits = len(input_list[0])
    searched_list = input_list
    current_bit_position = 0
    while current_bit_position < number_bits:
        most_common_digit = most_common_digits_balanced(searched_list)
        reference_list: List[Optional[int]] = (
            most_common_digit
            if use_most_common_digit
            else binary_not_digit_list_noneable(most_common_digit)
        )
        digit_searched_or_none: Optional[int] = reference_list[current_bit_position]
        # equal number of 1 and 0 (marked as None) should filter on 1
        digit_searched: int = (
            int(use_most_common_digit)
            if digit_searched_or_none is None
            else digit_searched_or_none
        )
        filtered_list = [
            number
            for number in searched_list
            if number[current_bit_position] == str(digit_searched)
        ]
        if len(filtered_list) == 1:
            return digit_list_to_int([int(i) for i in filtered_list[0]])
        else:
            current_bit_position += 1
            searched_list = filtered_list
    raise ValueError("No number matched the bit criteria for oxygen generator")


def solution2(input_list: List[str]) -> int:
    r"""Solve day3 part 2

    >>> solution2(["00100", "11110", "10110", "10111", "10101", "01111", "00111",
    ...            "11100", "10000", "11001", "00010", "01010"])
    230
    >>> solution2(["00100\n", "11110\n", "10110\n", "10111", "10101", "01111", "00111",
    ...            "11100", "10000", "11001", "00010", "01010"])
    230
    """
    numbers_list = [number_str.strip() for number_str in input_list]
    oxygen_rating = bit_criteria(numbers_list, True)
    co2_rating = bit_criteria(numbers_list, False)
    return oxygen_rating * co2_rating


def solve1_stringlist(input_str: str) -> int:
    """Convert list to proper format and solve day3 solution1"""
    return solution1(to_string_list(input_str))


def solve2_stringlist(input_str: str) -> int:
    """Convert list to proper format and solve day3 solution2"""
    return solution2(to_string_list(input_str))
