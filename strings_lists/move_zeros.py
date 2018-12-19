"""
Type: lists
Source: Leetcode (Easy)
Prompt: Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
1. You must do this in-place without making a copy of the array.
2. Minimize the total number of operations.

Examples:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Parameters:
- nums: list of ints

Returns: None. Modify the input list in-place.
"""

import unittest

def move_zeros(nums):
    """ 
    Naive, iterative, easy to read. Might be against the rules with the pop and append.
    t: O(n)
    s: O(1)
    """
    i = 0
    j = len(nums) - 1
    while i <= j:
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
            j -= 1
        else:
            i += 1

def move_zeros_iterative(nums):
    """ 
    Improved iterative method.
    t: O(n)
    s: O(1)
    """
    zero_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            if i > zero_pos: #make sure it's not the same element before swapping
                nums[i], nums[zero_pos] = nums[zero_pos], nums[i]
            zero_pos += 1

def move_zeros_pythonic(nums):
    """ 
    Pythonic, using extended slicing.
    t: O(n)
    s: O(1)
    """
    zero_count = nums.count(0)
    nums[:] = [i for i in nums if i != 0]
    nums += [0]*zero_count

def move_zeros_sort(nums):
    """ 
    Using Python built-in methods.
    t: O(nlogn)
    s: O(n)
    """
    return nums.sort(key=bool, reverse=True)


class MoveZerosTests(unittest.TestCase):

    def test_move_zeros(self):
        nums1 = [1, 0, 2, 0, 5]
        nums2 = [0, 0, 0]
        nums3 = [0, 0, 0, 1]
        move_zeros(nums1)
        move_zeros(nums2)
        move_zeros(nums3)
        self.assertEqual(nums1, [1, 2, 5, 0, 0])
        self.assertEqual(nums2, [0, 0, 0])
        self.assertEqual(nums3, [1, 0, 0, 0])

    def test_move_zeros_iterative(self):
        nums1 = [1, 0, 2, 0, 5]
        nums2 = [0, 0, 0]
        nums3 = [0, 0, 0, 1]
        move_zeros_iterative(nums1)
        move_zeros_iterative(nums2)
        move_zeros_iterative(nums3)
        self.assertEqual(nums1, [1, 2, 5, 0, 0])
        self.assertEqual(nums2, [0, 0, 0])
        self.assertEqual(nums3, [1, 0, 0, 0])

    def test_move_zeros_pythonic(self):
        nums1 = [1, 0, 2, 0, 5]
        nums2 = [0, 0, 0]
        nums3 = [0, 0, 0, 1]
        move_zeros_pythonic(nums1)
        move_zeros_pythonic(nums2)
        move_zeros_pythonic(nums3)
        self.assertEqual(nums1, [1, 2, 5, 0, 0])
        self.assertEqual(nums2, [0, 0, 0])
        self.assertEqual(nums3, [1, 0, 0, 0])

    def test_move_zeros_sort(self):
        nums1 = [1, 0, 2, 0, 5]
        nums2 = [0, 0, 0]
        nums3 = [0, 0, 0, 1]
        move_zeros_sort(nums1)
        move_zeros_sort(nums2)
        move_zeros_sort(nums3)
        self.assertEqual(nums1, [1, 2, 5, 0, 0])
        self.assertEqual(nums2, [0, 0, 0])
        self.assertEqual(nums3, [1, 0, 0, 0])

if __name__ == '__main__':
    unittest.main()
