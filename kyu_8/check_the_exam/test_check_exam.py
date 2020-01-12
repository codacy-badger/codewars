#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS ARRAYS NUMBERS BASIC LANGUAGE FEATURES

import unittest
import allure
from utils.log_func import print_log
from kyu_8.check_the_exam.check_exam import check_exam


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Check the exam')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class CheckExamTestCase(unittest.TestCase):
    """
    Testing check_exam function
    """

    def test_check_exam(self):
        """
        Testing check_exam function

        The function should return the score
        for this array of answers, giving +4
        for each correct answer, -1 for each
        incorrect answer, and +0 for each blank
        answer(empty string).
        :return:
        """

        allure.dynamic.title("Testing check_exam function")
        allure.dynamic.severity(allure.severity_level.CRITICAL)

        with allure.step("Enter arr1 and arr2 and verify the output"):

            data = [
                (["a", "a", "b", "b"], ["a", "c", "b", "d"], 6),
                (["a", "a", "c", "b"], ["a", "a", "b", ""], 7),
                (["a", "a", "b", "c"], ["a", "a", "b", "c"], 16),
                (["b", "c", "b", "a"], ["", "a", "a", "c"], 0),
            ]

            for arr1, arr2, expected in data:

                print_log(arr1=arr1,
                          arr2=arr2,
                          expected=expected)

                self.assertEqual(expected,
                                 check_exam(arr1, arr2))
