#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# BUGS REGULAR EXPRESSIONS DECLARATIVE PROGRAMMING ADVANCED LANGUAGE FEATURES FUNDAMENTALS STRINGS

import allure
import unittest
from utils.log_func import print_log
from kyu_5.not_very_secure.alphanumeric import alphanumeric


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Advanced Language Features")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Not very secure')
class AlphanumericTestCase(unittest.TestCase):
	"""
	Testing alphanumeric function
	"""

	def test_alphanumeric(self):
		"""
		Testing alphanumeric function with
		various test inputs

		The string has the following conditions
		to be alphanumeric only:

		1. At least one character ("" is not valid)
		2. Allowed characters are uppercase / lowercase
		   latin letters and digits from 0 to 9
		3. No whitespaces / underscore / special chars
		:return:
		"""

		allure.dynamic.title("Testing alphanumeric function")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		with allure.step("Enter test string and verify the output"):

			data = [
				("hello world_", False),
				("PassW0rd", True),
				("     ", False)
			]

			for password, expected in data:

				print_log(password=password,
				          expected=expected)

				self.assertEqual(expected,
				                 alphanumeric(password))
