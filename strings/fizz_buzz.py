"""
Type: strings, lists
Source: Leetcode (Easy)
Prompt: Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. 
For numbers which are multiples of both three and five output “FizzBuzz”.

Examples:
n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]


Parameters:
- n: int

Returns: list
"""

from collections import OrderedDict
import unittest

def fizz_buzz(n):
	"""
	Pythonic list comprehension
	t: O(n)
	s: O(1)
	"""
	return ['Fizz'*(not i%3) + 'Buzz'*(not i%5) or str(i) for i in range(1, n+1)]

def fizz_buzz_robust(n):
	"""
	Hash the options for extensibility (adding more rules)
	"""
	converter = OrderedDict([(3, 'Fizz'), (5, 'Buzz')])

	output = []
	for i in range(1, n+1):
		s = ''
		for k in converter.keys():
			s += converter[k] * (not i%k)
		if s == '':
			s = str(i)

		output.append(s)

	return output




class FizzBuzzTests(unittest.TestCase):
	TEST_OUTPUT = [
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
	]

	def test_fizz_buzz(self):
		self.assertEqual(fizz_buzz(15), self.TEST_OUTPUT)

	def test_fizz_buzz_robust(self):
		self.assertEqual(fizz_buzz_robust(15), self.TEST_OUTPUT)


if __name__ == '__main__':
    unittest.main()