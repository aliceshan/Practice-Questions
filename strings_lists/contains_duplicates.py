"""
Type: list, hash tables
Source: Leetcode (Easy)
Prompt: Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Examples:
Input: [1,2,3,1]
Output: true

Input: [1,2,3,4]
Output: false

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

Notes:
- Don't assume list won't be empty

Parameters:
- nums: list of ints

Returns: boolean
"""

import collections
import unittest

def has_dups(nums):
	''' Uses Python built-in method.
	t: O(n)
	s: O(n)
	'''
    if len(nums) <= 1:
        return False
    
    counter = collections.Counter(nums)
    return any(c > 1 for c in counter.values())


def has_dups_hash(nums):
	''' Creates hash table from scratch.
	t: O(n)
	s: O(n)
	'''
    if len(nums) <= 1:
        return False
    
    counter = {}
    for n in nums:
        counter[n] = counter.get(n,0) + 1
        
    return any(c > 1 for c in counter.values())

def has_dups_set(nums):
	'''
	Uses set and compares lengths.
	t: O(n)
	s: O(n)
	'''
	return len(nums) != len(set(nums))

def has_dups_sort(nums):
	'''
	Uses Python built-in sort
	t: O(nlogn)
	s: O(n) - timsort worst case
	'''
    if len(nums) <= 1:
        return False
    
    snums = sorted(nums)
    for i in range(len(snums) - 1):
        if snums[i] == snums[i+1]:
            return True
        
    return False

def has_dups_naive(nums):
	'''
	Naive method.
	t: O(n^2)
	s: O(1)
	'''
	for i in range(len(nums)):
		for j in range(i+1, range(len(nums))):
			if nums[i] == nums[j]:
				return True
	return False



