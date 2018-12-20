"""
Type: lists, recursion
Source: Leetcode (Easy)
Prompt: Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Examples:
Input: [3,2,3]
Output: 3

Input: [2,2,1,1,1,2,2]
Output: 2

Parameters:
- nums: list of ints

Returns: int, the majority element
"""

import unittest

def majority_element(nums):
	"""
	Uses the Boyer-Moore majority vote algorithm.
	Note that this algorithm depends on the fact that the majority element appears more than n/2 times
	t: O(n)
	s: O(1)
	"""
	counter = 0
	maj = None
	for num in nums:
		if counter == 0:
			maj = num
		if maj == num:
			counter += 1
		else:
			counter -= 1
	return maj

def majority_element_map(nums):
	"""
	Keeps track of element count in a hashmap.
	t: O(n)
	s: O(n)
	"""
	counter = {}
	for num in nums:
		counter[num] = counter.get(num,0) + 1

	for k, v in counter.items():
		if v > len(nums)/2:
			return k

def majority_element_map_counter(nums):
	"""
	Same as above hashmap implementation, but uses Python built-in collections.Counter.
	t: O(n)
	s: O(n)
	"""
	from collections import Counter
	maj = Counter(nums).most_common(1) #[(element, count),]
	return maj[0][0] 

def majority_element_sorting(nums):
	"""
	Uses Python built-in sorted function.
	t: O(nlogn) - timsort 
	s: O(n) - based on timsort implementation details
	"""
	return sorted(nums)[len(nums)//2]

def majority_element_recursion(nums):
	"""
	Recursive method using divide and conquer.
	Keeps track of indices rather than list slices to avoid using extra space.
	t: O(nlogn) - each iteration of the helper function takes potentially 2n
	s: O(logn) - size of the recursion stack
	"""
	def find_majority(vals, l, h):
		if l == h:
			return vals[l]

		mid = (h-l)//2 + l
		left_maj = find_majority(vals, l, mid)
		right_maj = find_majority(vals, mid+1, h)
		if left_maj == right_maj:
			return left_maj
		else:
			left_count = len([i for i in vals[l:h+1] if i == left_maj])
			right_count = len([i for i in vals[l:h+1] if i == right_maj])
			
			return left_maj if left_count > right_count else right_maj

	return find_majority(nums, 0, len(nums)-1)


class MajorityElementTests(unittest.TestCase):
	
	def setUp(self):
		self.nums = [2,2,1,1,1,2,2]
		self.expected_val = 2

	def test_majority_element(self):
		self.assertEqual(majority_element(self.nums), self.expected_val)

	def test_majority_element_map(self):
		self.assertEqual(majority_element_map(self.nums), self.expected_val)

	def test_majority_element_map_counter(self):
		self.assertEqual(majority_element_map_counter(self.nums), self.expected_val)

	def test_majority_element_sorting(self):
		self.assertEqual(majority_element_sorting(self.nums), self.expected_val)

	def test_majority_element_recursion(self):
		self.assertEqual(majority_element_recursion(self.nums), self.expected_val)

if __name__ == '__main__':
    unittest.main()

