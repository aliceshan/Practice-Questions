"""
Type: linked_lists
Source: Cracking the Coding Interview Q2.2
Prompt: Implement an algorithm to find the kth to last element of a singly linked list.

Notes:
- Assumes 1st to last = list[-1], 2nd to last = list[-2], ...

Parameters:
- head: Node, the head of the linked list
- k: the "k"th to last node to find

Returns: kth to last element of the linked list, None if list is not k nodes long
"""

import unittest

class Node:
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

def kth_to_last_node(head, k):
	""" Iterative approach: get a spacing of k between 2 pointers i and j, and then iterate until the end of the list.
	t: O(n)
	s: O(1)
	"""
	i = head
	j = head

	# initialize a distance of k between nodes i and j
	for _ in range(k - 1):
		if j.next != None:
			j = j.next
		else:
			return None

	# find the end of the list
	while j.next != None:
		i = i.next
		j = j.next

	return i


class KthToLastTests(unittest.TestCase):

	def test_kth_to_last_node(self):
		node1 = Node(value=1)
		node2 = Node(value=2)
		node3 = Node(value=3)
		node4 = Node(value=2)
		node5 = Node(value=5)

		node1.next = node2
		node2.next = node3
		node3.next = node4
		node4.next = node5

		output = kth_to_last_node(node1, 2)
		self.assertEqual(output, node4)

		output = kth_to_last_node(node1, 1)
		self.assertEqual(output, node5)

		output = kth_to_last_node(node1, 6)
		self.assertEqual(output, None)


if __name__ == '__main__':
    unittest.main()
