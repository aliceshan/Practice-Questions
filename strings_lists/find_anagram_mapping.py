"""
Type: lists, hash
Source: Leetcode (Easy)
Prompt: Given two lists Aand B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the elements in A.
We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.
These lists A and B may contain duplicates. If there are multiple answers, output any of them.

For example, given
A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
We should return
[1, 4, 3, 2, 0]
as P[0] = 1 because the 0th element of A appears at B[1], and P[1] = 4 because the 1st element of A appears at B[4], and so on.
Note:
A, B have equal lengths in range [1, 100].
A[i], B[i] are integers in range [0, 10^5].

Parameters:
- a, b: lists of ints

Returns: list of ints
"""


def anagram_map(a, b):
	""" Uses hash table.
	t: O(n)
	s: O(n)
	"""
	mapb = {}
	for i in range(len(b)):
		mapb.setdefault(b[i], []).append(i)

	print(mapb)
	return [mapb[num].pop() for num in a]

print(anagram_map([1,2,3], [3,1,2]))