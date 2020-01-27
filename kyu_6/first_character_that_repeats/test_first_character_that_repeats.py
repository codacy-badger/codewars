#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS

import unittest
import allure
from utils.log_func import print_log
from kyu_6.first_character_that_repeats.first_character_that_repeats import first_dup


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('First character that repeats')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class FirstDupTestCase(unittest.TestCase):
    """
    Testing first_dup function

    Find the first character that repeats
    in a String and return that character.
    """

    def test_first_dup_none(self):
        """
        Test string with no duplicate chars
        :return:
        """

        allure.dynamic.title("String with no duplicate chars")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Pass string with no repeating chars"):
            string = 'like'
            expected = None

            print_log(string=string, expected=expected)

            self.assertEqual(first_dup(string), expected)

        with allure.step("Pass string with no repeating chars"):
            string = 'bar'
            expected = None

            print_log(string=string, expected=expected)

            self.assertEqual(first_dup(string), expected)

    def test_first_dup_mixed(self):
        """
        Test string with mixed type of chars
        :return:
        """

        allure.dynamic.title("String with mixed type of chars")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Input consist of mixed type of chars"):
            string = '1a2b3a3c'
            expected = 'a'

            print_log(string=string, expected=expected)

            self.assertEqual(first_dup(string), expected)

        with allure.step("Input consist of alphabet chars and spaces"):
            string = 'ode to joy'
            expected = 'o'

            print_log(string=string, expected=expected)

            self.assertEqual(first_dup(string), expected)

    def test_first_alpha_only(self):
        """
        Test string with alphabet chars only
        :return:
        """
        allure.dynamic.title("String with alphabet chars only")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Input consist of alphabet chars only"):
            string = 'tweet'
            expected = 't'

            print_log(string=string, expected=expected)

            self.assertEqual(first_dup(string), expected)

    def test_first_space(self):
        """
        Repeating char is a space
        :return:
        """
        allure.dynamic.title("String alphabet chars and spaces")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Input consist of alphabet chars and spaces"):
            string = 'Ode to Joy'
            expected = ' '

            print_log(string=string, expected=expected)

            self.assertEqual(first_dup(string), expected)

    def test_first_no_alpha(self):
        """
        Test string with no alphabet chars
        :return:
        """

        allure.dynamic.title("String with no alphabet chars")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Pass string with digits only"):
            string = '123123'
            expected = '1'

            print_log(string=string, expected=expected)

            self.assertEqual(first_dup(string), expected)

        with allure.step("Pass string with special chars only"):
            string = '!@#$!@#$'
            expected = '!'

            print_log(string=string, expected=expected)

            self.assertEqual(first_dup(string), expected)
