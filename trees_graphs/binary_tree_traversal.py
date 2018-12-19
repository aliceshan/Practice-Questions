"""
Type: trees, recursion, DFS

Notes:
- Binary tree traversals are specific implementations of DFS.
"""

class Node:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


def in_order_traversal(node):
	"""
	Left descendants first, then current node, then right descendants.
	In binary search trees, this will visit nodes in ascending order.
	"""
	if node != None:
		in_order_traversal(node.left)
		visit(node)
		in_order_traversal(node.right)

def pre_order_traversal(node):
	"""
	Current node first, then left descendants, then right descendants.
	"""
	if node != None:
		visit(node)
		in_order_traversal(node.left)
		in_order_traversal(node.right)

def post_order_traversal(node):
	"""
	All descendants first, then current node.
	"""
	if node != None:
		in_order_traversal(node.left)
		in_order_traversal(node.right)
		visit(node)

def visit(node):
	"""
	Can implement additional functionality for visits here.
	"""
	print("Visited node {}, val {}".format(node, node.value))
	