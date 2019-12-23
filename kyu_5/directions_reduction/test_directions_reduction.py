#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS

import unittest
import allure
from kyu_5.directions_reduction.directions_reduction import dirReduc
from utils.log_func import print_log


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Directions Reduction')
class DirectionsReductionTestCase(unittest.TestCase):
	"""
	Testing dirReduc function
	"""

	def test_directions_reduction(self):
		"""
		Test a function dirReduc which will take an array of
		strings and returns an array of strings with the needless
		directions removed (W<->E or S<->N side by side).

		The Haskell version takes a list of directions with
		data Direction = North | East | West | South.

		The Clojure version returns nil when the path is
		reduced to nothing.

		The Rust version takes a slice of enum Direction
		{NORTH, SOUTH, EAST, WEST}.
		:return:
		"""

		allure.dynamic.title("Testing dirReduc function")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Enter test data (list) and verify the output"):
			data = [
				(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"],
				 ['WEST']),
				(["NORTH", "WEST", "SOUTH", "EAST"],
				 ["NORTH", "WEST", "SOUTH", "EAST"])
			]

			for d in data:
				array = d[0]
				expected = d[1]
				print_log(array=array, expected=expected)
				self.assertListEqual(expected, dirReduc(array))

