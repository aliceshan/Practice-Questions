"""
Type: Graphs, recursion
"""

class Node:

	def __init__(self, value=None, neighbors=None):
		self.value = value
		self.neighbors = neighbors or []
		self.visited = False

def dfs(root):
	""" 
	Simple depth first search.
	"""
	if not root:
		return

	visit(root)
	root.visited = True
	for node in root.neighbors:
		if not node.visited:
			dfs(node)


def visit(node):
	"""
	Can implement for further functionality.
	"""
	print("Visited node {}, value {}".format(node, node.value))
