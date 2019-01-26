"""
Type: lists
Source: Leetcode (Medium)
Prompt: Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.

Examples:

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

Parameters:
- nums: list of ints

Returns: None
"""

def next_permutation(nums):
	'''
	t: O(n)
	s: O(1)
	'''
	i = len(nums) - 1
	while i > 0 and nums[i] <= nums[i-1]:
		i -= 1

	if nums[i] > nums[i-1]:
		j = i
		while j < len(nums) and nums[j] > nums[i-1]:
		j += 1

	nums[i-1], nums[j-1] = nums[j-1], nums[i-1]
	nums[i:] = reversed(nums[i:])

	else:
		nums.reverse()