"""
Type: bit manipulation
Source: Cracking the Coding Interview Q5.1
Prompt: You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to insert M into N such that M starts at bit j and ends at bit i. 
You can assume that the bits j through i have enough space to fit all of M. That is, if M = 10011, you can assume that there are at least 5 bits between j and i.
You would not, for example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.

Examples:
Input: N = 10000000000, M = 10011, i = 2, j = 6
Output: N = 10001001100

Parameters:
- n, m, j, i: ints

Returns: int
"""

import unittest

def insert_bits(n, m, j, i):
	'''
	1. Create a mask to clear bits j through i in n.
	2. Shift m up i positions.
	3. | n and m.
	'''

	mask = (-1 << j + 1) | ~(-1 << i)
	return (n & mask) | (m << i)


class InsertBitsTests(unittest.TestCase):

	def test_insert_bits(self):

		n1 = int('10000000000', 2)
		m1 = int('10011', 2)
		self.assertEqual(insert_bits(n1, m1, 6, 2), int('10001001100', 2))
		self.assertEqual(insert_bits(n1, m1, 7, 3), int('10010011000', 2))

		n2 = int('11111111111', 2)
		self.assertEqual(insert_bits(n2, m1, 6, 2), int('11111001111', 2))
		self.assertEqual(insert_bits(n2, m1, 7, 3), int('11110011111', 2))


if __name__ == '__main__':
	unittest.main()