"""
Type: lists
Source: Leetcode (Medium)
Prompt: Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Examples:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Parameters:
- matrix: list of lists of ints

Returns: list
"""

def spiralOrder(self, matrix):
	''' Go in levels.
	t: O(mn)
	s: O(1) - not counting output
	'''
	if not matrix:
		return []
	
	output = []
	r1, c1 = 0, 0
	r2, c2 = len(matrix)-1, len(matrix[0])-1
	
	while r1 <= r2 and c1 <= c2:
		for c in range(c1, c2+1):
			output.append(matrix[r1][c])
		for r in range(r1+1, r2+1):
			output.append(matrix[r][c2])
		if r1 < r2 and c1 < c2:
			for c in range(c2-1, c1-1, -1):
				output.append(matrix[r2][c])
			for r in range(r2-1, r1, -1):
				output.append(matrix[r][c1])
		r1 += 1
		c1 += 1
		r2 -= 1
		c2 -= 1

	return output