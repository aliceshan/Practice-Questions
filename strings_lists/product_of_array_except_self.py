"""
Type: lists
Source: Leetcode (Medium)
Prompt: Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
Note: Please solve it without division and in O(n).
Follow up: Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

Examples:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Parameters:
- nums: list of ints

Returns: list of ints
"""

import unittest

def product_except_self(nums):
	output = []
	m = 1
	for i in range(len(nums)):
		output.append(m)
		m *= nums[i]
	m = 1
	for i in range(len(nums)-1, -1, -1):
		output[i] *= m
		m *= nums[i]

	return output

class ProductExceptSelfTests(unittest.TestCase):

	def setUp(self):
		self.nums1 = [1, 2, 3, 4]
		self.ev1 = [24, 12, 8, 6]

	def test_product_except_self(self):
		self.assertEqual(product_except_self(self.nums1), self.ev1)


if __name__ == '__main__':
	unittest.main()