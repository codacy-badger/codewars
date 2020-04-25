import unittest
import allure
from utils.log_func import print_log
from kyu_6.find_the_odd_int.find_the_odd_int import find_it

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Find the odd int')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class FindTheOddIntTestCase(unittest.TestCase):
    """
    Testing find_it function
    """

    def test_something(self):
        """
        Sample testing.
        Expected result is 5
        :return:
        """

        allure.dynamic.title("Find the int that appears "
                             "an odd number of times")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Assert the result"):
            lst = [20, 1, -1, 2, -2, 3, 3, 5, 5,
                   1, 2, 4, 20, 4, -1, -2, 5]
            expected = 5

            print_log(list=lst, expected=expected)

            self.assertEqual(find_it(lst), expected)
