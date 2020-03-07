#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from utils.is_prime import is_prime
from typing import Set, Dict


def has_subpattern(string: str) -> bool:
    """
    String subpattern recognition II

    if a subpattern has been used, it will be repeated at least twice,
    meaning the subpattern has to be shorter than the original string;

    the strings you will be given might or might not be created
    repeating a given subpattern, then shuffling the result.

    :param string:
    :return:
    """

    primes: Set[int] = set()
    length = len(string)
    char_dict: Dict[str, int] = dict()

    for char in string:

        if char not in char_dict:
            char_dict[char] = string.count(char)

            if char_dict[char] == 1:
                return False

            if char_dict[char] in primes or is_prime(char_dict[char]):
                primes.add(char_dict[char])
                if length % char_dict[char] != 0:
                    return False

    return True
