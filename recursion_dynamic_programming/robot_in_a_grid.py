"""
Type: Dynamic programming, graphs
Source: Cracking the Coding Interview (8.2)
Prompt: Imagine a rovot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them.
Design an algorithm to find a path for the robot from the top left to the bottom right.
"""

import unittest

def get_path(grid):
	''' Dynamic programming, going backwards from (r,c). Like backwards DFS. 
	Note: finds a path, not necessarily shortest path.
	'''
	if not grid:
		return None

	path = []
	failed = set()
	if _get_path(grid, len(grid) - 1, len(grid[0]) - 1, path, failed):
		return path

	return None

def _get_path(grid, row_idx, col_idx, path, failed):
	if row_idx < 0 or col_idx < 0 or not grid[row_idx][col_idx]: #if we are out of bounds, or the step is "off limits"
		return False

	point = row_idx * len(grid[0]) + col_idx # points are counted to the right then down, starting at 0
	if point in failed:
		return False

	if point == 0 or _get_path(grid, row_idx, col_idx - 1, path, failed) or _get_path(grid, row_idx - 1, col_idx, path, failed):
		path.append(point)
		return True

	failed.add(point)
	return False

def get_path_dfs(grid):
	''' TODO: complete this implementation.
	DFS going forwards from (0,0). Same as above but going in the opposite direction.
	Note: finds a path, not necessarily shortest path.
	'''
	path = []
	visited = set() # could also use a list of length r*c to keep track of indices, but avg lookup time is the same
	if _get_path_dfs(grid, 0, 0, path, visited):
		return reversed(path)

	return None

def _get_path_dfs(grid, row_idx, col_idx, path, visited):
	if row_idx >= len(grid) or col_idx >= len(grid[0]) or not grid[row_idx][col_idx]:
		return False

	point = row_idx * len(grid[0]) + col_idx
	if point == (len(grid)-1)*(len(grid[0])-1) or _get_path_dfs(grid, row_idx + 1, col_idx, path, visited) or _get_path_dfs(grid, row_idx, col_idx + 1, path, visited):
		return True

class GetPathTests(unittest.TestCase):

	def setUp(self):
		# empty grid
		self.grid1 = [[]]
		self.ev1 = None

		# one element grid
		self.grid2 = [[True]]
		self.ev2 = [0]

		# grid with no path
		self.grid3 = [
			[True, False, False], 
			[False, True, True]]
		self.ev3 = None

		#grid with one path
		self.grid4 = [
			[True, False, False], 
			[True, True, True],
			[False, False, True],
			]
		self.ev4 = [0, 3, 4, 5, 8]

	def test_get_path(self):
		self.assertEqual(get_path(self.grid1), self.ev1)
		self.assertEqual(get_path(self.grid2), self.ev2)
		self.assertEqual(get_path(self.grid3), self.ev3)
		self.assertEqual(get_path(self.grid4), self.ev4)


if __name__ == '__main__':
	unittest.main()
