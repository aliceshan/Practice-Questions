# TODO: throw error when trying to pop/peek empty stack

class Stack:

	def __init__(self, init_list=None):
		self.stack = init_list or []

	def push(self, val):
		self.stack.append(val)

	def pop(self):
		if not self.stack.is_empty():
			return self.stack.pop()

	def peek(self):
		if not self.stack.is_empty():
			return self.stack[-1]

	def is_empty(self):
		return self.stack == []

	def size(self):
		return len(self.stack)