"""
Type: stacks
Source: Cracking the Coding Interview Q3.2
Prompt: Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? 
Push, pop, min should all operate in O(1) time.

Notes:
- Additional functionality to initialize with a list is additional, not part of the prompt.

"""

from simple_stack import Stack

class MinStack(Stack):

	def __init__(self, init_list=None):
		super( MinStack, self ).__init__()
		self.min_vals = self.init_min_vals()


	def init_min_vals(self):
		min_list = []
		for i in self.stack:
			if min_list == []:
				min_list.append(i)
			else:
				if min_list[i] >= i:
					min_list.append(i)
		return min_list

	def min(self):
		return self.mins[-1]

	def remove_min_val(val):
		if self.min_vals[-1] == val:
			return self.min_vals.pop()

	def pop(self):
		popped = self.stack.pop()
		self.remove_min_val(popped)
