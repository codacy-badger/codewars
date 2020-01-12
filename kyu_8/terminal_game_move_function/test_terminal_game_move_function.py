#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.terminal_game_move_function.terminal_game_move_function import move


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Math")
@allure.sub_suite("Unit Tests")
@allure.feature("Calculation")
@allure.story('Grasshopper - Terminal game move function')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class MoveTestCase(unittest.TestCase):
    """
    Testing move function
    """

    def test_move(self):
        """
        The player rolls the dice and moves the number
        of spaces indicated by the dice two times.

        Pass position and roll and compare the output
        to the expected result
        :return:
        """
        allure.dynamic.title("move function tests")
        allure.dynamic.severity(allure.severity_level.NORMAL)

        with allure.step("Test start position zero"):
            position = 0
            roll = 4
            expected = 8

            print_log(position=position,
                      roll=roll,
                      expected=expected)
            self.assertEqual(move(position, roll), expected)

        with allure.step("Test start position even number"):
            position = 3
            roll = 6
            expected = 15

            print_log(position=position,
                      roll=roll,
                      expected=expected)
            self.assertEqual(move(position, roll), expected)

        with allure.step("Test start position odd number"):
            position = 2
            roll = 5
            expected = 12

            print_log(position=position,
                      roll=roll,
                      expected=expected)
            self.assertEqual(move(position, roll), expected)
