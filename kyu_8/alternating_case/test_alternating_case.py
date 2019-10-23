#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.alternating_case.alternating_case import to_alternating_case


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('altERnaTIng cAsE <=> ALTerNAtiNG CaSe')
class AlternatingCaseTestCase(unittest.TestCase):
	"""
	Testing to_alternating_case function
	"""

	def test_alternating_case(self):
		"""
		Testing to_alternating_case function
		:return:
		"""

		allure.dynamic.title("Testing to_alternating_case function")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("Enter test string and verify the output"):

			data = [
				("hello world", "HELLO WORLD"),
				("HELLO WORLD", "hello world"),
				("HeLLo WoRLD", "hEllO wOrld"),
				("hello WORLD", "HELLO world"),
				("12345", "12345"),
				("1a2b3c4d5e", "1A2B3C4D5E"),
				("String.prototype.toAlternatingCase",
				 "sTRING.PROTOTYPE.TOaLTERNATINGcASE"),
				("Hello World", "hELLO wORLD"),
				("altERnaTIng cAsE", "ALTerNAtiNG CaSe")
			]

			for d in data:
				string = d[0]
				expected = d[1]

				print_log(string=string, expected=expected)
				self.assertEqual(to_alternating_case(string), expected)
