#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def powers(n) -> list:
	"""
	Return an array of numbers
	(that are a power of 2)
	for which the input "n" is the sum
	:param n:
	:return:
	"""

	lst = list()
	power = 0

	while (2 ** power) <= n:
		lst.append(2 ** power)
		power += 1

	if lst[-1] > n:
		i = -2
	else:
		i = -1

	result = list()
	while sum(result) != n:
		if sum(result) + lst[i] <= n:
			result.append(lst[i])
		i -= 1

	return sorted(result)
