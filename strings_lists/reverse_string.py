"""
Type: strings, recursion
Source: Leetcode (Easy)
Prompt: Write a function that takes a string as input and returns the string reversed.

Examples:
Input: "hello"
Output: "olleh"

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"

Parameters:
- s: string to be reversed

Returns: reversed string
"""

import unittest

def reverse_string(s):
	""" 
	Built-in function reversed.
	t: O(n)
	s: O(1)
	"""
	return "".join(reversed(s))

def reverse_string_slicing(s):
	"""
	Extended slicing.
	t: O(n)
	s: O(1)
	"""
	return s[::-1]

def reverse_string_recursive(s):
	"""
	Recursion.
	t: O(n)
	s: O(1)
	"""
	if len(s) == 1:
		return s

	return reverse_string_recursive(s[len(s)//2:]) + reverse_string_recursive(s[:len(s)//2])


class KthToLastTests(unittest.TestCase):

	def test_reverse_string(self):
		self.assertEqual(reverse_string("hello world"), "dlrow olleh")

	def test_reverse_string_slicing(self):
		self.assertEqual(reverse_string("hello world"), "dlrow olleh")

	def test_reverse_string_recursive(self):
		self.assertEqual(reverse_string("hello world"), "dlrow olleh")


if __name__ == '__main__':
    unittest.main()


