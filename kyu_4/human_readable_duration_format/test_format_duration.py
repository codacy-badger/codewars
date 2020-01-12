#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS FORMATS STRINGS DATES/TIME FORMATTING

import allure
import unittest
from utils.log_func import print_log
from kyu_4.human_readable_duration_format.format_duration import format_duration


@allure.epic('4 kyu')
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Human readable duration format')
@allure.tag('ALGORITHMS', 'FORMATS', 'STRINGS', 'DATES/TIME', 'FORMATTING')
@allure.link(url='https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python',
             name='Source/Kata')
class FormatDurationTestCase(unittest.TestCase):
	"""
	Testing format_duration
	"""

	def test_format_duration(self):
		"""
		Test a function which formats a duration,
		given as a number of seconds, in a human-friendly way.

		The function must accept a non-negative integer.
		If it is zero, it just returns "now". Otherwise,
		the duration is expressed as a combination of years,
		days, hours, minutes and seconds.
		:return:
		"""

		allure.dynamic.title("Testing format_duration")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Enter seconds and verify the output"):
			test_data = [
				(1, "1 second"),
				(62, "1 minute and 2 seconds"),
				(120, "2 minutes"),
				(3600, "1 hour"),
				(3662, "1 hour, 1 minute and 2 seconds"),
				(15731080, '182 days, 1 hour, 44 minutes and 40 seconds'),
				(132030240, '4 years, 68 days, 3 hours and 4 minutes'),
				(205851834, '6 years, 192 days, 13 hours, 3 minutes and 54 seconds'),
				(253374061, '8 years, 12 days, 13 hours, 41 minutes and 1 second'),
				(242062374, '7 years, 246 days, 15 hours, 32 minutes and 54 seconds'),
				(101956166, '3 years, 85 days, 1 hour, 9 minutes and 26 seconds'),
				(33243586, '1 year, 19 days, 18 hours, 19 minutes and 46 seconds'),
				(9041160, '104 days, 15 hours and 26 minutes'),
			]

			for seconds, expected in test_data:
				print_log(seconds=seconds,
				          expected=expected)

				self.assertEqual(expected,
				                 format_duration(seconds))
