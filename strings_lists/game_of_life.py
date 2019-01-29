"""
Type: lists, bit manipulation
Source: Leetcode (Medium)
Prompt: According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
Given a board with m by n cells, each cell has an initial state live (1) or dead (0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. 
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, 
which would cause problems when the active area encroaches the border of the array. How would you address these problems?

Examples:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

Parameters:
- board: list of list of ints

Returns: None
"""

def game_of_life(board):
    '''
    t: O(n)
    s: O(1)
    '''
    for r in range(len(board)):
        for c in range(len(board[0])):
            neighbors = living_neighbors(r, c, board)
            if neighbors == 3 and board[r][c] == 0:
                board[r][c] = 2
            elif neighbors in (2, 3) and board[r][c] == 1:
                board[r][c] = 3

    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] = board[r][c] >> 1

def living_neighbors(r, c, board):
    neighbors = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    living = 0
    for nr, nc in neighbors:
        if 0 <= r+nr < len(board) and 0 <= c+nc < len(board[0]):
            living += board[r+nr][c+nc] & 1
    return living