"""
Type: lists, dynamic programming
Source: Leetcode (Easy)
Prompt: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Examples:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Parameters:
- nums: list of ints

Returns: int
"""

import unittest

def max_sum(nums):
	''' Kadane's algorithm. 
	t: O(n)
	s: O(1)
	'''
	max_sum = float('-inf')
	curr_sum = 0
	for n in nums:
		curr_sum = max(n, curr_sum + n) # set curr_sum to n if curr_sum is negative
		max_sum = max(max_sum, curr_sum)
	return max_sum

def _max_crossing_sum(nums, left, mid, right):
	''' Helper for max_sum_recursive.
	'''
	left_max = float('-inf')
	curr_max = 0
	for i in range(mid, left-1, -1): # go backwards from mid to left.
		curr_max += nums[i]
		left_max = max(left_max, curr_max)

	right_max = float('-inf')
	curr_max = 0
	for i in range(mid+1, right+1):
		curr_max += nums[i]
		right_max = max(right_max, curr_max)

	return left_max + right_max


def _max_sum_recursive(nums, left, right):
	''' Helper for max_sum_recursive.,
	'''
	if left == right:
		return nums[left]

	mid = (left + right) // 2
	return max(
		_max_sum_recursive(nums, left, mid),
		_max_sum_recursive(nums, mid+1, right),
		_max_crossing_sum(nums, left, mid, right))

def max_sum_recursive(nums):
	''' Divide and conquer. Assumes non-empty list.
	t: O(nlogn)
	s: O(logn)
	'''
	return _max_sum_recursive(nums, 0, len(nums)-1)


class MaxSumTests(unittest.TestCase):

	def setUp(self):
		self.nums1 = [-2,1,-3,4,-1,2,1,-5,4]
		self.ev1 = 6
		self.nums2 = [-9,-3,-5,-2,-3]
		self.ev2 = -2

	def test_max_sum(self):
		self.assertEqual(max_sum(self.nums1), self.ev1)
		self.assertEqual(max_sum(self.nums2), self.ev2)

	def test_max_sum_recursive(self):
		self.assertEqual(max_sum_recursive(self.nums1), self.ev1)
		self.assertEqual(max_sum_recursive(self.nums2), self.ev2)

if __name__ == '__main__':
	unittest.main()
