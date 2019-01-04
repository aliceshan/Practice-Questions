"""
Type: linked lists
Source: Leetcode (Easy)
Prompt: Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.

Examples:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""

class Node:

	def __init__(self, val=None, next_node=None):
		self.val = val
		self.next = next_node

def has_cycle(head):
	''' 2 pointers.
	t: O(n) - fast pointer will go through the list at most 2 times.
	s: O(1)
	'''
	slow = head
	fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if slow == fast:
			return True 

	return False


def has_cycle_hashed(head):
	''' hash set.
	t: O(n)
	s: O(n)
	'''
	visited = set()
	while head:
		if head in visited:
			return True
		visited.add(head)
		head = head.next

	return False


