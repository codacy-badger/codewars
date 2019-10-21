#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS  BASIC LANGUAGE FEATURES  STRINGS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.remove_first_and_last_character.remove_char import remove_char


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Remove First and Last Character')
class RemoveCharTestCase(unittest.TestCase):
	"""
	Testing remove_char function
	"""

	def test_remove_char(self):
		"""
		Test that 'remove_char' function
		removes the first and
        last characters of a string.
		:return:
		"""

		allure.dynamic.title("Testing remove_char function")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Pass 'eloquent' string and verify the output"):
			string = 'eloquent'
			expected = 'loquen'

			print_log(string=string,
			          expected=expected)

			self.assertEqual(remove_char(string), expected)

		with allure.step("Pass 'country' string and verify the output"):
			string = 'country'
			expected = 'ountr'

			print_log(string=string,
			          expected=expected)

			self.assertEqual(remove_char(string), expected)

		with allure.step("Pass 'person' string and verify the output"):
			string = 'person'
			expected = 'erso'

			print_log(string=string,
			          expected=expected)

			self.assertEqual(remove_char(string), expected)

		with allure.step("Pass 'place' string and verify the output"):
			string = 'place'
			expected = 'lac'

			print_log(string=string,
			          expected=expected)

			self.assertEqual(remove_char(string), expected)

		with allure.step("Pass 'ok' string and verify the output"):
			string = 'ok'
			expected = ''

			print_log(string=string,
			          expected=expected)

			self.assertEqual(remove_char(string), expected)
