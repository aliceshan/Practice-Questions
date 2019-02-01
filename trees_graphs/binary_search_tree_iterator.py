"""
Type: binary search tree, DFS
Source: Leetcode (Medium)
Prompt: Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.
next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

Parameters: 
- root: TreeNode
"""

import collections

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class BSTIterator(object):

	def __init__(self, root):
		''' Add smaller elements to the stack as we progress.
		t: next - O(h), has_next = O(1)
		s: O(h)
		'''
		self.root = root
		self.stack = []

	def next(self):
		while self.root:
			self.stack.append(self.root)
			self.root = self.root.left
		smallest = self.stack.pop()
		self.root = smallest.right
		return smallest.val

	def has_next(self):
		return len(self.stack) > 0 or self.root != None

class BSTIterator2(object):

	def __init__(self, root):
		''' Initialize entire tree into queue.
		t: initialize - O(n), next/has_next - O(1)
		s: O(n)
		'''
		self.root = root
		self.queue = collections.deque()
		self.initialize(root)

	def initialize(self, node):
		if node:
			if node.left:
				self.initialize(node.left)
			self.queue.append(node.val)
			if node.right:
				self.initialize(node.right)

	def next(self):
		return self.queue.popleft()

	def has_next(self):
		return len(self.queue) > 0

