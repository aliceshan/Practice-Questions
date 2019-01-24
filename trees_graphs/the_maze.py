"""
Type: graphs
Source: Leetcode (Medium)
Prompt: There is a ball in a maze with empty spaces and walls. 
The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.
The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. 
You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Examples:

Input 1: a maze represented by a 2D array
0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)
Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Input 1: a maze represented by a 2D array
0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0
Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)
Output: false
Explanation: There is no way for the ball to stop at the destination.

Parameters:
- maze: list of lists of ints (1s and 0s)
- start: list of ints (2 elements)
- destination: list of ints (2 elements)

Returns: boolean
"""


import collections
import unittest

def has_path_bfs(maze, start, destination):
	''' BFS method.
	t: O(mn) - worst case go through every element
	s: O(mn) - visited list duplicates maze, queue size in worst case
	'''
	visited = [[False for element in row] for row in maze]
	dirs = [[-1,0], [1,0], [0,-1], [0,1]]
	q = collections.deque([start])
	m, n = len(maze), len(maze[0])

	visited[start[0]][start[1]] = True
	while len(q) != 0:
		r, c = q.popleft()
		if [r,c] == destination:
			return True

		for dr, dc in dirs:
			newr, newc = r, c
			while 0 <= newr+dr < m and 0 <= newc+dc < n and maze[newr+dr][newc+dc] == 0:
				newr += dr
				newc += dc

			if not visited[newr][newc]:
				visited[newr][newc] = True
				q.append([newr, newc])

	return False


def has_path_dfs(maze, start, destination):
	''' DFS method.
	t: O(mn) - worst case go through every element
	s: O(mn) - visited list duplicates maze, queue size in worst case
	'''
	visited = [[False for element in row] for row in maze]
	dirs = [[-1,0], [1,0], [0,-1], [0,1]]
	m, n = len(maze), len(maze[0])

	def search(sr, sc):
		visited[sr][sc] = True
		if [sr, sc] == destination:
			return True

		for dr, dc in dirs:
			newr, newc = sr, sc
			while 0 <= newr+dr < m and 0 <= newc+dc < n and maze[newr+dr][newc+dc] == 0:
				newr += dr
				newc += dc
			if not visited[newr][newc] and search(newr, newc):
				return True
		return False

	return search(start[0], start[1])


class HasPathTests(unittest.TestCase):


	def setUp(self):
		self.m1 = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
		self.s1 = [0,4]
		self.d1 = [4,4]
		self.ev1 = True
		self.s2 = [0,4]
		self.d2 = [3,2]
		self.ev2 = False
		self.s3 = [0,4]
		self.d3 = [1,2]
		self.ev3 = True

	def test_has_path_bfs(self):
		self.assertEqual(has_path_bfs(self.m1, self.s1, self.d1), self.ev1)
		self.assertEqual(has_path_bfs(self.m1, self.s2, self.d2), self.ev2)
		self.assertEqual(has_path_bfs(self.m1, self.s3, self.d3), self.ev3)


	def test_has_path_dfs(self):
		self.assertEqual(has_path_dfs(self.m1, self.s1, self.d1), self.ev1)
		self.assertEqual(has_path_dfs(self.m1, self.s2, self.d2), self.ev2)
		self.assertEqual(has_path_dfs(self.m1, self.s3, self.d3), self.ev3)

if __name__ == '__main__':
	unittest.main()




print(dfs(m, s, d))