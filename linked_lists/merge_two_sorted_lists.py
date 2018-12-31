"""
Type: linked lists, recursion
Source: Leetcode (Easy)
Prompt: Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Examples:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Parameters:
	- l1, l2: ListNode

Returns: ListNode
"""

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def merge_lists(l1, l2):
	'''
	Iterative method.
	t: O(n + m)
	s: O(1)
	'''
	mock_head = ListNode(0)
	prev = mock_head
	while l1 and l2:
		if l1.val <= l2.val:
			prev.next = l1
			l1 = l1.next
		else:
			prev.next = l2
			l2 = l2.next
		prev = prev.next

	if l1 is not None:
		prev.next = l1
	else:
		prev.next = l2

	return mock_head.next

def merge_lists_recursive(l1, l2):
	'''
	Recursive method.
	t: O(n + m)
	s: O(n + m)
	'''
	if l1 is None:
		return l2
	elif l2 is None:
		return l1

	if l1.val <= l2.val:
		l1.next = merge_lists_recursive(l1.next, l2)
		return l1
	else:
		l2.next = merge_lists_recursive(l1, l2.next)
		return l2


