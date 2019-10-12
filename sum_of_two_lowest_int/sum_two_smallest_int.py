#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def sum_two_smallest_numbers(numbers) -> int:
    """
    Returns the sum of the two lowest
    positive numbers given an array of
    minimum 4 positive integers.
    :param numbers:
    :return:
    """
    numbers.sort()
    return numbers[0] + numbers[1]
