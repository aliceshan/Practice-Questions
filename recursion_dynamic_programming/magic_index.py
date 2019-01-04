"""
Type: Recursion
Source: Cracking the Coding Interview (8.3)
Prompt: A magic index in an array A[1...n-1] is defined to be an index such that A[i] = i.
Given a sorted array of distinct inteers, write a method to find a magic index, if one exists, in array A.
Follow up: What if the values are not distinct?

Parameters:
- a: list

Returns: int
"""

import unittest

def magic_index(a):
	''' Recursive method.
	t: O(logn)
	s: O(logn)
	'''
	return _magic_index(a, 0, len(a)-1)

def _magic_index(a, left, right):
	if right < left:
		return -1

	mid = (left + right)//2
	if a[mid] == mid:
		return mid
	elif a[mid] > mid:
		return _magic_index(a, left, mid-1)
	else:
		return _magic_index(a, mid+1, right)

def magic_index_iterative(a):
	''' Iterative implementation of recursive method.
	t: O(logn)
	s: O(1)
	'''
	left = 0
	right = len(a) - 1
	while left <= right:
		mid = (left + right)//2
		if a[mid] == mid:
			return mid
		elif a[mid] > mid:
			right = mid - 1
		else:
			left = mid + 1
	return -1


def magic_index_iterative2(a):
	''' Improved brute force. Works for non-distinct lists.
	t: O(n)
	s: O(1)
	'''
	i = 0
	while i < len(a):
		if a[i] == i:
			return i
		elif a[i] > i:
			i = a[i]
		else:
			i += 1
	return -1


#TODO: recursive method accounting for non-distinct lists.


class MagicIndexTests(unittest.TestCase):

	def setUp(self):
		self.a1 = [-5,1,3,4,5]
		self.ev1 = 1
		self.a2 = [1,2,3,4,5]
		self.ev2 = -1
		self.a3 = [1,2,5,5,5,5]
		self.ev3 = 5

	def test_magic_index(self):
		self.assertEqual(magic_index(self.a1), self.ev1)
		self.assertEqual(magic_index(self.a2), self.ev2)

	def test_magic_index_iterative(self):
		self.assertEqual(magic_index_iterative(self.a1), self.ev1)
		self.assertEqual(magic_index_iterative(self.a2), self.ev2)

	def test_magic_index_iterative2(self):
		self.assertEqual(magic_index_iterative2(self.a1), self.ev1)
		self.assertEqual(magic_index_iterative2(self.a2), self.ev2)
		self.assertEqual(magic_index_iterative2(self.a3), self.ev3)


if __name__ == '__main__':
	unittest.main()
