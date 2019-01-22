"""
Type: recursion, strings, lists
Source: Leetcode (Medium)
Prompt: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Examples:
Given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

Parameters:
- n: int

Returns: list of strings
"""

import unittest

def generate_parentheses(n):
	''' Backtracking.
	t: ?
	s: O(n) - recursion stack, not including output list
	'''
	if n == 0:
		return []
	output = []
	def _generate(s='', left=0, right=0):
		if len(s) == 2*n:
			output.append(s)
			return

		if left < n:
			# we've generated fewer than n left brackets, so can add more
			_generate(s+'(', left+1, right)
		if right < left:
			# we've generated fewer right brackets than left brackets, so can add a right and keep the validity
			_generate(s+')', left, right+1)

	_generate()
	return output

def generate_parentheses_naive(n):
	''' Recursion with extra steps.
	At n, there are 2 types of combinations. 
	e.g. for n=3, we have [ "n=1,n=2", "n=2,n=1", "(n=2)" ]
	t: 
	s: O(n) - memo and recursion stack
	'''
	def _parentheses(n, memo):
		if n == 0:
			return []
		if n == 1:
			return ['()']
		if memo.get(n):
			return memo[n]
		else:
			output = set()
			for i in range(1, n//2 + 1):
				l1 = _parentheses(i, memo)
				l2 = _parentheses(n-i, memo)
				for j in l1:
					for k in l2:
						output.add(j+k)
						output.add(k+j)

			for item in _parentheses(n-1, memo):
				output.add('(' + item + ')')

			memo[n] = list(output)
		return output

	return _parentheses(n, {})


class GenerateParenthesesTests(unittest.TestCase):

	def setUp(self):
		self.n1 = 0
		self.ev1 = []
		self.n2 = 3
		self.ev2 = ["((()))","(()())","(())()","()(())","()()()"]


	def test_generate_parentheses(self):
		output1 = generate_parentheses(self.n1)
		output2 = generate_parentheses(self.n2)
		self.assertEqual(len(output1), len(self.ev1))
		self.assertEqual(set(output1), set(self.ev1))
		self.assertEqual(len(output2), len(self.ev2))
		self.assertEqual(set(output2), set(self.ev2))

	def test_generate_parentheses_naive(self):
		output1 = generate_parentheses_naive(self.n1)
		output2 = generate_parentheses_naive(self.n2)
		self.assertEqual(len(output1), len(self.ev1))
		self.assertEqual(set(output1), set(self.ev1))
		self.assertEqual(len(output2), len(self.ev2))
		self.assertEqual(set(output2), set(self.ev2))


if __name__ == '__main__':
	unittest.main()

