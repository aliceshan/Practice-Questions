"""
Type: lists (biggest subarray with 2 distinct types)
Source: Leetcode (Medium)
Prompt: In a row of trees, the i-th tree produces fruit with type tree[i].
You start at any tree of your choice, then repeatedly perform the following steps:
Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.
You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.
What is the total amount of fruit you can collect with this procedure?
1 <= tree.length <= 40000
0 <= tree[i] < tree.length

Examples:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.
 
Parameters:
- tree: list of ints

Returns: int
"""

import unittest

def total_fruit(tree):
	''' Sliding window.
	t: O(n)
	s: O(1) - hash table has at most 3 keys
	'''
	count = {}
	total_max = 0
	i = 0
	for j, val in enumerate(tree):
		count[val] = count.get(val, 0) + 1
		while len(count) > 2:
			count[tree[i]] -= 1
			if count[tree[i]] == 0:
				del count[tree[i]]
			i += 1
		total_max = max(total_max, j - i + 1)

	return total_max

def total_fruit2(tree):
	''' Keeping track with multiple variables.
	'''
	total_max = curr_max = curr_num = 0
	curr_type = -1
	types = set()

	for val in tree:
		if val in types:
			if val != curr_type:
				curr_type = val
				curr_num = 0
			curr_num += 1
			curr_max += 1
		else:
			types = set([curr_type, val])
			curr_max = curr_num + 1
			curr_type = val
			curr_num = 1
		total_max = max(curr_max, total_max)

	return total_max


class TotalFruitTests(unittest.TestCase):

	def setUp(self):
		self.tree1 = [1,2,1]
		self.ev1 = 3
		self.tree2 = [0,1,2,2]
		self.ev2 = 3
		self.tree3 = [3,3,3,1,2,1,1,2,3,3,4]
		self.ev3 = 5

	def test_total_fruit(self):
		self.assertEqual(total_fruit(self.tree1), self.ev1)
		self.assertEqual(total_fruit(self.tree2), self.ev2)
		self.assertEqual(total_fruit(self.tree3), self.ev3)

	def test_total_fruit2(self):
		self.assertEqual(total_fruit2(self.tree1), self.ev1)
		self.assertEqual(total_fruit2(self.tree2), self.ev2)
		self.assertEqual(total_fruit2(self.tree3), self.ev3)


if __name__ == '__main__':
	unittest.main()

