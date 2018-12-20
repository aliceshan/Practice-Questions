"""
Type: bit manipulation, math
Source: Cracking the Coding Interview Q5.2
Prompt: Given a real number between 0 and 1 (e.g. 0.72) that is passed in as a double, print the binary representation.
If the number cannot be represented accurately in binary with at most 32 characters, print "ERROR".

Parameters:
- num, float.

Returns: str, binary representation of the input.
"""

import unittest

def print_binary(num):
	''' 
	Iterative method.
	Multiply num by 2 to get binary digit, repeat until all values are accounted for.
	'''
	output = '.'
	val = num
	while val > 0:
		if len(output) >= 32:
			return 'ERROR'

		x = round(val * 2, 5)
		if x >= 1:
			output += '1'
			val = x - 1
		else:
			output += '0'
			val = x

	return output


class PrintBinaryTests(unittest.TestCase):

	def test_print_binary(self):
		self.assertEqual(print_binary(.625), '.101')
		self.assertEqual(print_binary(1/3), 'ERROR')


if __name__ == '__main__':
	unittest.main()