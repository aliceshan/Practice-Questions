"""
Type: lists
Source: Leetcode (Medium)
Prompt: Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, 
such that the container contains the most water.
Note: You may not slant the container and n is at least 2.

Examples:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

Parameters: 
- height: list of ints

Returns: int
"""

import unittest

def max_area(height):
	''' Iterative, uses 2 pointers.
	t: O(n)
	s: O(1)
	'''
	max_area = 0
	left = 0
	right = len(height) - 1
	while left < right:
		curr_area = min(height[left], height[right])*(right-left)
		max_area = max(max_area, curr_area)
		if height[left] <= height[right]:
			left += 1
		else:
			right -= 1
	return max_area

def max_area_naive(height):
	''' Naive iterative method.
	t: O(n^2)
	s: O(1)
	'''
	max_area = 0
	for i in range(len(height)):
		for j in range(i+1, len(height)):
			curr_area = min(height[i], height[j])*(j-i)
			max_area = max(max_area, curr_area)
	return max_area

class MaxAreaTests(unittest.TestCase):

	def setUp(self):
		self.height1 = [1,8,6,2,5,4,8,3,7]
		self.ev1 = 49
		self.height2 = [1,5,7,1,5]
		self.ev2 = 15
		self.height3 = [1,3]
		self.ev3 = 1

	def test_max_area(self):
		self.assertEqual(max_area(self.height1), self.ev1)
		self.assertEqual(max_area(self.height2), self.ev2)
		self.assertEqual(max_area(self.height3), self.ev3)

	def test_max_area_naive(self):
		self.assertEqual(max_area_naive(self.height1), self.ev1)
		self.assertEqual(max_area_naive(self.height2), self.ev2)
		self.assertEqual(max_area_naive(self.height3), self.ev3)

if __name__ == '__main__':
	unittest.main()
