"""
Type: trees, recursion, DFS
Source: Leetcode (Easy)
Prompt: Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
A leaf is a node with no children.

Examples:
Given binary tree [3,9,20,null,null,15,7],
return its depth = 3.

Parameters:
- root: TreeNode, root of the tree

Returns: int, max depth of the tree 
"""

import unittest

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def max_depth(root):
	""" Recursive method. DFS.
	t: O(n) - looks at every node once
	s: O(logn) to O(n) - balanced tree vs completely unbalanced tree
	"""

	if root == None:
		return 0

	else:
		return max(max_depth(root.left), max_depth(root.right)) + 1


def max_depth_iterative(root):
	""" Iterative method. DFS.
	t: O(n) - looks at every node once
	s: O(n) - the stack
	"""

	stack = []
	if root is not None:
		stack.append((1, root))

	depth = 0
	while stack != []:
		curr, node = stack.pop()
		if node is not None:
			depth = max(depth, curr)
			stack.append((curr + 1, node.left))
			stack.append((curr + 1, node.right))

	return depth


class MaxDepthTests(unittest.TestCase):

	def test_max_depth(self):
		node1 = TreeNode(1)
		node2 = TreeNode(2)
		node3 = TreeNode(3)
		node4 = TreeNode(4)
		node5 = TreeNode(5)
		node6 = TreeNode(6)

		node1.left = node2
		node1.right = node3
		node3.left = node4
		node3.right = node5
		node5.left = node6

		self.assertEqual(max_depth(node1), 4)
		self.assertEqual(max_depth(node6), 1)

	def test_max_depth_iterative(self):
		node1 = TreeNode(1)
		node2 = TreeNode(2)
		node3 = TreeNode(3)
		node4 = TreeNode(4)
		node5 = TreeNode(5)
		node6 = TreeNode(6)

		node1.left = node2
		node1.right = node3
		node3.left = node4
		node3.right = node5
		node5.left = node6

		self.assertEqual(max_depth_iterative(node1), 4)
		self.assertEqual(max_depth_iterative(node6), 1)


if __name__ == '__main__':
    unittest.main()

