"""
Type: lists
Source: Leetcode (Hard)
Prompt: Given an unsorted integer array, find the smallest missing positive integer.
Your algorithm should run in O(n) time and uses constant extra space.

Examples:
Input: [1,2,0]
Output: 3

Input: [3,4,-1,1]
Output: 2

Input: [7,8,9,11,12]
Output: 1

Parameters:
- nums: list of ints

Returns: int
"""


def firstMissingPositive(self, nums):
    '''
    Note how this accounts for the empty list case.
    t: O(n)
    s: O(n) - can be O(1) if list can be modified in place.
    '''
    pointer = [0] * (len(nums) + 1)
    for n in nums:
        if n >= 1 and n <= len(nums):
            pointer[n] = n
    for i in range(len(pointer)):
        if pointer[i] != i:
            return i
        
    return i + 1