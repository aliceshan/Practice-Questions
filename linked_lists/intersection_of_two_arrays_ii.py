"""
Type: lists
Source: Leetcode (Easy)
Prompt: Given two arrays, write a function to compute their intersection.
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

Examples:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Parameters:
- nums1, nums2: lists of ints 

Returns: list of ints
"""

import unittest

def intersect(nums1, nums2):
	''' iterative method.
	t: O(n)
	s: O(n)
	'''
	map1, map2 = {}, {}
	output = []
	for i in nums1:
	    map1[i] = map1.get(i, 0) + 1
	for i in nums2:
	    map2[i] = map2.get(i, 0) + 1
	    
	if len(map1) >= len(map2):
	    map1, map2 = map2, map1
	for k, v in map1.items():
	    if map2.get(k):
	        output.extend([k]*min(map1[k], map2[k]))
	return output

def intersect_sorted(nums1, nums2):
	''' Assumes inputs are sorted in ascending order.
	t: O(n)
	s: O(1)
	'''
	output = []
	i = 0
	j = 0
	while i < len(nums1) and j < len(nums2):
		if nums1[i] < nums2[j]:
			i += 1
		elif nums1[i] > nums2[j]:
			j += 1
		else:
			output.append(nums1[i])
			i += 1
			j += 1
	return output


class IntersectTests(unittest.TestCase):

	def setUp(self):
		self.nums11 = [1,2,2,1]
		self.nums21 = [2, 2]
		self.ev1 = [2, 2]

		self.nums12 = [4,9,5]
		self.nums22 = [9,4,9,8,4]
		self.ev2 = [4, 9]

	def test_intersect(self):
		self.assertEqual(intersect(self.nums11, self.nums21), self.ev1)
		self.assertEqual(intersect(self.nums12, self.nums22), self.ev2)

	def test_intersect_sorted(self):
		self.assertEqual(intersect_sorted(sorted(self.nums11), sorted(self.nums21)), self.ev1)
		self.assertEqual(intersect_sorted(sorted(self.nums12), sorted(self.nums22)), self.ev2)


