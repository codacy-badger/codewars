#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def generate_hashtag(s: str):
	"""
	The Hashtag Generator.

	1. It must start with a hashtag (#).
	2. All words must have their first letter capitalized.
	3. If the final result is longer than 140 chars it must return false.
	4. If the input or the result is an empty string it must return false.

	:param s:
	:return:
	"""
	if len(s.strip()) < 1:
		return False

	result = '#{}'.format(''.join([string.capitalize()
	                               for string in s.split(' ')
	                               if string.strip() != '']))

	return False if len(result) > 140 else result
