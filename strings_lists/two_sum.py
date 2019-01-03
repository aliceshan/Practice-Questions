"""
Type: lists
Source: Leetcode (Easy)
Prompt: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Examples: 
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Parameters:
- nums: list of ints
- target: int

Returns: list of ints
"""

import unittest

def two_sum(nums, target):
	''' Hash table.
	t: O(n)
	s: O(n)
	'''
	vals_map = {}
	for i in range(len(nums)):
		j = vals_map.get(target - nums[i])
		if j is not None and i != j:
			return [j, i]

		vals_map[nums[i]] = i

	return []


def two_sum_naive(nums, target):
	'''Naive brute force.
	t: O(n^2)
	s: O(1)
	'''
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if nums[i] + nums[j] == target:
				return [i, j]

	return []


class TwoSumTests(unittest.TestCase):

	def setUp(self):
		self.nums1 = [2, 7, 11, 15]
		self.target1 = 9
		self.ev1 = [0, 1]

		self.nums2 = [1, 5, -3]
		self.target2 = -2
		self.ev2 = [0, 2]

	def test_two_sum(self):
		self.assertEqual(two_sum(self.nums1, self.target1), self.ev1)
		self.assertEqual(two_sum(self.nums2, self.target2), self.ev2)

	def test_two_sum_naive(self):
		self.assertEqual(two_sum_naive(self.nums1, self.target1), self.ev1)
		self.assertEqual(two_sum_naive(self.nums2, self.target2), self.ev2)


if __name__ == '__main__':
	unittest.main()

