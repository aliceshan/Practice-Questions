"""
Type: lists, math, bit manipulation
Source: Leetcode (Easy)
Prompt: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Examples:
Input: [3,0,1]
Output: 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Parameters:
- nums, list of ints

Returns: int, missing value
"""

import unittest

def missing_num(nums):
	''' bit manipulation.
	t: O(n)
	s: O(1)
	'''
	missing_val = len(nums)
	for idx, val in enumerate(nums):
		missing_val ^= idx ^ val

	return missing_val


def missing_num_set(nums):
	''' set difference.
	t: O(n)
	s: O(n)
	'''
	return (set(range(len(nums) + 1)) - set(nums)).pop()

def missing_num_sum(nums):
	''' sum of ints up to n.
	Note: may overflow if sum is too big
	t: O(n)
	s: O(1)
	'''
	n = len(nums)
	return n*(n + 1)//2 - sum(nums)

class MissingNumberTests(unittest.TestCase):


	def setUp(self):
		self.nums1 = [3,0,1]
		self.ev1 = 2
		self.nums2 = [9,6,4,2,3,5,7,0,1]
		self.ev2 = 8
		self.nums3 = [0]
		self.ev3 = 1

	def test_missing_num(self):
		self.assertEqual(missing_num(self.nums1), self.ev1)
		self.assertEqual(missing_num(self.nums2), self.ev2)
		self.assertEqual(missing_num(self.nums3), self.ev3)

	def test_missing_num_set(self):
		self.assertEqual(missing_num_set(self.nums1), self.ev1)
		self.assertEqual(missing_num_set(self.nums2), self.ev2)
		self.assertEqual(missing_num_set(self.nums3), self.ev3)

	def test_missing_num_sum(self):
		self.assertEqual(missing_num_sum(self.nums1), self.ev1)
		self.assertEqual(missing_num_sum(self.nums2), self.ev2)
		self.assertEqual(missing_num_sum(self.nums3), self.ev3)

if __name__ == '__main__':
	unittest.main()

