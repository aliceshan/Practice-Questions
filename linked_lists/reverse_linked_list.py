"""
Type: linked lists, recursion
Source: Leetcode (Easy)
Prompt: Reverse a singly linked list.

Examples:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Notes:
- Do not assume that head exists.

Parameters:
- head: Node, head of the list.

Returns: Node, new head of the list.
"""

import unittest

class Node:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next


def reverse_list(head):
	"""
	Iterative method.
	t: O(n)
	s: O(1)
	"""
	prev = None
	while head:
		curr = head
		head = head.next
		curr.next = prev
		prev = curr

	return prev

def reverse_list_condensed(head):
	""" 
	Iterative method, condensed. Looks cooler, a bit harder to understand.
	t: O(n)
	s: O(1)
	"""
	prev = None
	while head:
		head.next, prev, head = prev, head, head.next
	return prev


def reverse_list_recursive(head):
	""" 
	Recursive method
	t: O(n)
	s: O(n) - recursion stack goes n levels
	"""
	if not head or not head.next:
		return head
	newHead = reverse_list(head.next)
	head.next.next = head
	head.next = None
	return newHead


class ReverseListTests(unittest.TestCase):

    def test_reverse_list(self):
    	a, b, c = Node('a'), Node('b'), Node('c')
    	a.next = b
    	b.next = c
    	reverse_list(a)
    	self.assertEqual(c.next, b)
    	self.assertEqual(b.next, a)
    	self.assertEqual(a.next, None)

    	d = Node('d')
    	self.assertEqual(reverse_list(d), d)

    	self.assertEqual(reverse_list(None), None)

    def test_reverse_list_condensed(self):
    	a, b, c = Node('a'), Node('b'), Node('c')
    	a.next = b
    	b.next = c
    	reverse_list_condensed(a)
    	self.assertEqual(c.next, b)
    	self.assertEqual(b.next, a)
    	self.assertEqual(a.next, None)

    	d = Node('d')
    	self.assertEqual(reverse_list_condensed(d), d)

    	self.assertEqual(reverse_list_condensed(None), None)

    def test_reverse_list_recursive(self):
    	a, b, c = Node('a'), Node('b'), Node('c')
    	a.next = b
    	b.next = c
    	reverse_list_recursive(a)
    	self.assertEqual(c.next, b)
    	self.assertEqual(b.next, a)
    	self.assertEqual(a.next, None)

    	d = Node('d')
    	self.assertEqual(reverse_list_recursive(d), d)

    	self.assertEqual(reverse_list_recursive(None), None)


if __name__ == '__main__':
    unittest.main()

