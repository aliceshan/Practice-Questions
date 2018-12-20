"""
Type: strings, math
Source: Leetcode (Easy)
Prompt: Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Examples:
Input: "A"
Output: 1

Input: "AB"
Output: 28

Input: "ZY"
Output: 701

Parameters:
- s: string to be converted

Returns: int, converted from s
"""

import functools
import unittest

def title_to_number(s):
	"""
	Iterative method 1 (going right to left)
	t: 
	s: 
	"""
	val = 0
	for i in range(1, len(s)+1):
		val += (ord(s[-i]) - 64) * 26**(i-1)

	return val

def title_to_number_2(s):
	"""
	Iterative method 2 (going left to right)
	t:
	s:
	"""
	val = 0
	for i in s:
		val = val*26 + ord(i) - 64

	return val

def title_to_number_func(s):
	"""
	Functional method. (note: Python 3 recommends against using reduce due to lack of readability)
	t: 
	s:
	"""
	return functools.reduce(lambda x, y: x*26 + y, [ord(i) - 64 for i in s])


class TitleToNumberTests(unittest.TestCase):

	def setUp(self):
		self.s1 = 'A'
		self.ev1 = 1 
		self.s2 = 'AB'
		self.ev2 = 28
		self.s3 = 'ZY'
		self.ev3 = 701
		self.s4 = 'AAA'
		self.ev4 = 703

	def test_title_to_number(self):
		self.assertEqual(title_to_number(self.s1), self.ev1)
		self.assertEqual(title_to_number(self.s2), self.ev2)
		self.assertEqual(title_to_number(self.s3), self.ev3)
		self.assertEqual(title_to_number(self.s4), self.ev4)


	def test_title_to_number_2(self):
		self.assertEqual(title_to_number_2(self.s1), self.ev1)
		self.assertEqual(title_to_number_2(self.s2), self.ev2)
		self.assertEqual(title_to_number_2(self.s3), self.ev3)
		self.assertEqual(title_to_number_2(self.s4), self.ev4)

	def test_title_to_number_func(self):
		self.assertEqual(title_to_number_func(self.s1), self.ev1)
		self.assertEqual(title_to_number_func(self.s2), self.ev2)
		self.assertEqual(title_to_number_func(self.s3), self.ev3)
		self.assertEqual(title_to_number_func(self.s4), self.ev4)


if __name__ == '__main__':
	unittest.main()