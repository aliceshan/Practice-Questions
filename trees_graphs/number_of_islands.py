"""
Type: graphs
Source: Leetcode (Medium)
Prompt: Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Examples:

Input:
11110
11010
11000
00000
Output: 1

Input:
11000
11000
00100
00011
Output: 3

Parameters: 
- grid: list of lists of ints

Returns: int
"""

import unittest

def num_islands(grid):
	''' DFS.
	t: O(m*n)
	s: O(m*n)
	'''
	islands = 0
	visited = [[False] * len(grid[0]) for _ in range(len(grid))]
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if not visited[i][j] and grid[i][j] == '1':
				search((i,j), grid, visited)
				islands += 1
	return islands

def search(node, grid, visited):
	if node[0] < 0 or node[0] >= len(grid):
		return
	if node[1] < 0 or node[1] >= len(grid[0]):
		return
	if grid[node[0]][node[1]] == '0':
		return
	if visited[node[0]][node[1]]:
		return
	visited[node[0]][node[1]] = True

	search((node[0],node[1]-1), grid, visited)
	search((node[0]-1,node[1]), grid, visited)
	search((node[0],node[1]+1), grid, visited)
	search((node[0]+1,node[1]), grid, visited)


class NumIslandsTests(unittest.TestCase):

	def setUp(self):
		self.grid1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
		self.ev1 = 1
		self.grid2 = [["0","1","0"],["1","0","1"],["0","1","0"]]
		self.ev2 = 4

	def test_num_islands(self):
		self.assertEqual(num_islands(self.grid1), self.ev1)
		self.assertEqual(num_islands(self.grid2), self.ev2)

if __name__ == '__main__':
	unittest.main()