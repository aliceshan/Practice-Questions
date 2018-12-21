"""
Type: strings, hash tables
Source: Leetcode (Easy), Cracking the Coding Interview Q1.2
Prompt: Given two strings s and t, write a function to determine if t is an anagram of s.

Examples:
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false

Notes:
- whitespace counts
- not case sensitive

Parameters:
- s, t: strings

Returns: boolean
"""

import collections
import unittest

def is_anagram(s, t):
	'''
	Using Python standard library.
	t: O(n) - 3n: twice to create dicts, once to compare
	s: O(n) - 2n: 2 dicts
	'''
	return collections.Counter(s) == collections.Counter(t)


def is_anagram_hash(s, t):
	'''
	Creating hash tables from scratch.
	t: O(n)
	s: O(n)
	'''
	counter = {}
	for i in s:
		counter[i] = counter.get(i, 0) + 1
	for j in t:
		counter[j] = counter.get(j, 0) - 1

	return all(c == 0 for c in counter.values())

def is_anagram_sort(s, t):
	'''
	t: O(nlogn)
	s: O(n) - worst case for timsort
	'''
	return sorted(s) == sorted(t)


class AnagramTests(unittest.TestCase):

	def setUp(self):
		self.s1 = 'anagram'
		self.t1 = 'aangram'
		self.ev1 = True

		self.s2 = ''
		self.t2 = ''
		self.ev2 = True

		self.s3 = 'cat'
		self.t3 = 'cata'
		self.ev3 = False

	def test_is_anagram(self):
		self.assertEqual(is_anagram(self.s1, self.t1), self.ev1)
		self.assertEqual(is_anagram(self.s2, self.t2), self.ev2)
		self.assertEqual(is_anagram(self.s3, self.t3), self.ev3)

	def test_is_anagram_hash(self):
		self.assertEqual(is_anagram_hash(self.s1, self.t1), self.ev1)
		self.assertEqual(is_anagram_hash(self.s2, self.t2), self.ev2)
		self.assertEqual(is_anagram_hash(self.s3, self.t3), self.ev3)

	def test_is_anagram_sort(self):
		self.assertEqual(is_anagram_sort(self.s1, self.t1), self.ev1)
		self.assertEqual(is_anagram_sort(self.s2, self.t2), self.ev2)
		self.assertEqual(is_anagram_sort(self.s3, self.t3), self.ev3)

if __name__ == '__main__':
	unittest.main()