"""
Type: recursion, strings, lists
Source: Leetcode (Medium)
Prompt: Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Your answer can be in any order you want.

Examples:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Parameters:
- digits: string

Returns: list of strings
"""

import unittest

def letter_combos(digits):
	''' Backtracking.
	t: ?
	s: n
	'''
	if len(digits) == 0:
		return []

	mapping = {
		'2': ['a', 'b', 'c'],
		'3': ['d', 'e', 'f'],
		'4': ['g', 'h', 'i'],
		'5': ['j', 'k', 'l'],
		'6': ['m', 'n', 'o'],
		'7': ['p', 'q', 'r', 's'],
		'8': ['t', 'u', 'v'],
		'9': ['w', 'x', 'y', 'z'],
	}

	output = []
	def _generate(s, nums):
		if len(nums) == 0:
			output.append(s)
			return

		for c in mapping[nums[0]]:
			_generate(s+c, nums[1:])


	_generate('', digits)
	return output


class LetterCombosTests(unittest.TestCase):

	def setUp(self):
		self.digits1 = ''
		self.ev1 = []
		self.digits2 = '23'
		self.ev2 = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

	def test_letter_combos(self):
		self.assertEqual(letter_combos(self.digits1), self.ev1)
		self.assertEqual(letter_combos(self.digits2), self.ev2)

if __name__ == '__main__':
	unittest.main()