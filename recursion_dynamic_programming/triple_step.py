"""
Type: Dynamic programming, recursion
Source: Cracking the Coding Interview (8.1)
Prompt: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.

Parameters:
- n: int

Returns: int
"""

import unittest

def count_ways(n):
	''' Recursive method, includes memoization. Counts n=0 as 1 way.
	t: O(n)
	s: O(n)
	'''
	steps = [-1] * (n + 1)
	return count_ways_helper(n, steps)

def count_ways_helper(n, steps):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	else:
		if steps[n] == -1:
			steps[n] = count_ways_helper(n-1, steps) + count_ways_helper(n-2, steps) + count_ways_helper(n-3, steps)
		return steps[n]

def count_ways_iterative(n):
	''' Iterative method. Counts n=0 as 1 way.
	t: O(n)
	s: O(1)
	'''
	total_ways = 1
	one_step = 1
	two_step = 0
	three_step = 0
	for i in range(1, n+1):
		total_ways = one_step + two_step + three_step
		three_step = two_step
		two_step = one_step
		one_step = total_ways

	return total_ways

class CountWaysTests(unittest.TestCase):

	def setUp(self):
		self.n1 = 3
		self.ev1 = 4
		self.n2 = 4
		self.ev2 = 7
		self.n3 = 0
		self.ev3 = 1

	def test_count_ways(self):
		self.assertEqual(count_ways(self.n1), self.ev1)
		self.assertEqual(count_ways(self.n2), self.ev2)
		self.assertEqual(count_ways(self.n3), self.ev3)

	def test_count_ways_iterative(self):
		self.assertEqual(count_ways_iterative(self.n1), self.ev1)
		self.assertEqual(count_ways_iterative(self.n2), self.ev2)
		self.assertEqual(count_ways_iterative(self.n3), self.ev3)


if __name__ == '__main__':
    unittest.main()
