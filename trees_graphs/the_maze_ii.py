"""
Type: graphs
Source: Leetcode (Medium)
Prompt:
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. 
When the ball stops, it could choose the next direction.
Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. 
The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). 
If the ball cannot stop at the destination, return -1.
The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. 
The start and destination coordinates are represented by row and column indexes. 

Examples:

Input 1: a maze represented by a 2D array
0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0
Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)
Output: 12
Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Input 1: a maze represented by a 2D array
0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0
Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)
Output: -1
Explanation: There is no way for the ball to stop at the destination.

Parameters:
- maze: list of lists of ints (1s and 0s)
- start: list of ints (2 elements)
- destination: list of ints (2 elements)

Returns: int
"""


import collections
import heapq
import unittest


def shortest_distance_bfs(maze, start, destination):
    ''' BFS.
    t: O(mn*max(m,n)) - worst case full traversal. for each node, also worst case full depth.
    s: O(mn)
    '''
    q = collections.deque([start])
    dirs = [[-1,0], [1,0], [0,-1], [0,1]]
    m, n = len(maze), len(maze[0])
    distances = [[float('inf')]*len(maze[0]) for _ in range(len(maze))]

    distances[start[0]][start[1]] = 0
    while len(q) != 0:
        r, c = q.popleft()            
        for dr, dc in dirs:
            newr, newc = r, c
            steps = 0
            while 0 <= newr+dr < m and 0 <= newc+dc < n and maze[newr+dr][newc+dc] == 0:
                newr += dr
                newc += dc
                steps += 1

            if distances[r][c] + steps < distances[newr][newc]:
                distances[newr][newc] = distances[r][c] + steps
                q.append([newr, newc])

    dist = distances[destination[0]][destination[1]]
    return dist if dist != float('inf') else -1


def shortest_distance_dfs(maze, start, destination):
    ''' DFS.
    t: O(mn*max(m,n)) - worst case full traversal. for each node, also worst case full depth.
    s: O(mn)
    '''
    dirs = [[-1,0], [1,0], [0,-1], [0,1]]
    m, n = len(maze), len(maze[0])
    distances = [[float('inf')]*len(maze[0]) for _ in range(len(maze))]
    distances[start[0]][start[1]] = 0

    def search(r, c):
        for dr, dc in dirs:
            nr, nc = r, c
            steps = 0
            while 0 <= nr+dr < m and 0 <= nc+dc < n and maze[nr+dr][nc+dc] == 0:
                nr += dr
                nc += dc
                steps += 1
            if distances[r][c] + steps < distances[nr][nc]:
                distances[nr][nc] = distances[r][c] + steps
                search(nr, nc)

    search(start[0], start[1])
    dist = distances[destination[0]][destination[1]]
    return dist if dist != float('inf') else -1



def shortest_distance_dijkstra(maze, start, destination):
    ''' BFS using Dijkstra's.
    t: O(mn*log(mn))
    s: O(mn)
    '''
    distances = [[float('inf')]*len(maze[0]) for _ in range(len(maze))]
    dirs = [[-1,0], [1,0], [0,-1], [0,1]]
    m, n = len(maze), len(maze[0])

    def search(r, c):
        pq = []
        distances[r][c] = 0
        heapq.heappush(pq, (0, r, c))
        while len(pq) != 0:
            dist, nr, nc = heapq.heappop(pq)
            if distances[nr][nc] < dist:
                continue
            for dr, dc in dirs:
                nextr, nextc = nr, nc
                steps = 0
                while 0 <= nextr+dr < m and 0 <= nextc+dc < n and maze[nextr+dr][nextc+dc] == 0:
                    nextr += dr
                    nextc += dc
                    steps += 1

                if distances[nr][nc] + steps < distances[nextr][nextc]:
                    distances[nextr][nextc] = distances[nr][nc] + steps
                    heapq.heappush(pq, (distances[nextr][nextc], nextr, nextc))

    search(start[0], start[1])
    dist = distances[destination[0]][destination[1]]
    return dist if dist != float('inf') else -1


class HasPathTests(unittest.TestCase):


    def setUp(self):
        self.m1 = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
        self.s1 = [0,4]
        self.d1 = [4,4]
        self.ev1 = 12
        self.s2 = [0,4]
        self.d2 = [3,2]
        self.ev2 = -1
        self.s3 = [0,4]
        self.d3 = [1,2]
        self.ev3 = 9

    def test_shortest_distance_bfs(self):
        self.assertEqual(shortest_distance_bfs(self.m1, self.s1, self.d1), self.ev1)
        self.assertEqual(shortest_distance_bfs(self.m1, self.s2, self.d2), self.ev2)
        self.assertEqual(shortest_distance_bfs(self.m1, self.s3, self.d3), self.ev3)


    def test_has_path_dfs(self):
        self.assertEqual(shortest_distance_dfs(self.m1, self.s1, self.d1), self.ev1)
        self.assertEqual(shortest_distance_dfs(self.m1, self.s2, self.d2), self.ev2)
        self.assertEqual(shortest_distance_dfs(self.m1, self.s3, self.d3), self.ev3)

    def test_has_path_dijkstra(self):
        self.assertEqual(shortest_distance_dijkstra(self.m1, self.s1, self.d1), self.ev1)
        self.assertEqual(shortest_distance_dijkstra(self.m1, self.s2, self.d2), self.ev2)
        self.assertEqual(shortest_distance_dijkstra(self.m1, self.s3, self.d3), self.ev3)


if __name__ == '__main__':
    unittest.main()