
"""
Type: linked_lists
Source: Cracking the Coding Interview Q2.1
Prompt: Write code to remove duplicates from an unsorted linked list. FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?

Notes:
- Assumed that head is never None
- Assumed that list is singly linked

Parameters:
- head: Node, the head of the linked list

Returns: the head with duplicates removed
"""

import unittest

class Node:
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

def remove_dups(head):
	"""
	Uses a set to keep track of values that already exists in the linked list.
	t: O(n) - looks at every node once
	s: O(n) - worst case there are no duplicates, set s is size n
	"""
	
	# keep track of existing values
	s = set([head.value])

	n = head
	while n.next != None:
		if n.next.value in s:
			#this is a dup, remove it from the list
			n.next = n.next.next
		else:
			s.add(n.next.value)
			n = n.next

	return head

def remove_dups_no_space(head):
	"""
	Nested loops implementation without using extra space. Looks through entire list for dups of every node.
	t: O(n^2) - looks at every node n times
	s: O(1) - no extra space used
	"""

	curr = head
	while curr != None:
		search = curr
		while search.next != None:
			if curr.value == search.next.value:
				search.next = search.next.next
			else:
				search = search.next
		curr = curr.next

	return head


class RemoveDupsTests(unittest.TestCase):

	def test_remove_dups(self):
		node1 = Node(value=1)
		node2 = Node(value=2)
		node3 = Node(value=3)
		node4 = Node(value=2)
		node5 = Node(value=5)

		node1.next = node2
		node2.next = node3
		node3.next = node4
		node4.next = node5

		output = remove_dups(node1)

		self.assertEqual(node3.next, node5)
		self.assertEqual(output, node1)

	def test_remove_dups_no_space(self):
		node1 = Node(value=1)
		node2 = Node(value=2)
		node3 = Node(value=3)
		node4 = Node(value=2)
		node5 = Node(value=5)

		node1.next = node2
		node2.next = node3
		node3.next = node4
		node4.next = node5

		output = remove_dups_no_space(node1)

		self.assertEqual(node3.next, node5)
		self.assertEqual(output, node1)

if __name__ == '__main__':
    unittest.main()


