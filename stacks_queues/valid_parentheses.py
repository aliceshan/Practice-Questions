"""
Type: stacks, strings, lists 
Source: Leetcode (Easy)
Prompt: Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Examples:
Input: "()"
Output: true

Input: "()[]{}"
Output: true

Input: "(]"
Output: false

Input: "([)]"
Output: false

Input: "{[]}"
Output: true

Parameters:
- s: string

Returns: boolean
"""

def is_valid(s):
	''' Stack method.
	Note: Assumes all chars are valid.
	t: O(n)
	s: O(n)
	'''
	mapping = {')': '(', '}': '{', ']': '['}
	stack = []
	for c in s:
		if mapping.get(c):
			if len(stack) == 0 or mapping.get(c) != stack.pop():
	    		return False
		else:
			stack.append(c)

	return len(stack) == 0


