"""
Type: Graphs, queues
"""

from collections import deque

class Node:

	def __init__(self, value=None, neighbors=None):
		self.value = value
		self.neighbors = neighbors or []
		self.visited = False

def bfs(root):
	""" 
	Breadth first search while keeping track of distances to the root node (all edge weights are 1).
	If distances are not needed, change distance tracker to a simple marker for checking the node has been added to the queue.
	Uses Python built-in collections.deque for queue, can replace with list if needed.
	"""
	distances = {root: 0}
	queue = deque(root)

	while len(queue) != 0:
		node = queue.popleft()
		visit(node)
		for neighbor in node.neighbors:
			if not distances.get(neighbor):
				distances[neighbor] = distances[node] + 1
				queue.append(neighbor)

	return distances