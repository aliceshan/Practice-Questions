"""
Type: lists, dynamic programming
Source: Leetcode (Easy)
Prompt: Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

Examples:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Not 7-1 = 6, as selling price needs to be larger than buying price.

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Parameters:
- prices: list of ints

Returns: int
"""

import unittest

def max_profit(prices):
	'''
	Iterative one pass method.
	t: O(n)
	s: O(1)
	'''
	max_profit = 0
	if len(prices) <= 1:
		return max_profit

	buy_price = prices[0]
	for i in range(1, len(prices)):
		if prices[i] < buy_price:
			buy_price = prices[i]
		elif prices[i] - buy_price > max_profit:
			max_profit = prices[i] - buy_price

	return max_profit

def max_profit_kadanes(prices):
	'''
	Kadanes algorithm method.
	t: O(n)
	s: O(1)
	'''
	max_curr = 0
	max_profit = 0
	if len(prices) <= 1:
		return max_profit

	for i in range(1, len(prices)):
		max_curr = max(0, max_curr + prices[i] - prices[i-1])
		max_profit = max(max_profit, max_curr)

	return max_profit

def max_profit_naive(prices):
	'''
	Naive brute force method.
	t:O(n)
	s:O(1)
	'''
	profit = 0
	for i in range(len(prices)):
		for j in range(i+1, len(prices)):
			profit = max(profit, prices[j] - prices[i])

	return profit


class MaxProfitTests(unittest.TestCase):


	def setUp(self):
		self.prices1 = [7,1,5,3,6,4]
		self.ev1 = 5

		self.prices2 = [7,6,4,3,1]
		self.ev2 = 0

		self.prices3 = [7,3,5,1]
		self.ev3 = 2

		self.prices4 = []
		self.ev4 = 0

	def test_max_profit(self):
		self.assertEqual(max_profit(self.prices1), self.ev1)
		self.assertEqual(max_profit(self.prices2), self.ev2)
		self.assertEqual(max_profit(self.prices3), self.ev3)
		self.assertEqual(max_profit(self.prices4), self.ev4)

	def test_max_profit_kadanes(self):
		self.assertEqual(max_profit_kadanes(self.prices1), self.ev1)
		self.assertEqual(max_profit_kadanes(self.prices2), self.ev2)
		self.assertEqual(max_profit_kadanes(self.prices3), self.ev3)
		self.assertEqual(max_profit_kadanes(self.prices4), self.ev4)

	def test_max_profit_naive(self):
		self.assertEqual(max_profit_naive(self.prices1), self.ev1)
		self.assertEqual(max_profit_naive(self.prices2), self.ev2)
		self.assertEqual(max_profit_naive(self.prices3), self.ev3)
		self.assertEqual(max_profit_naive(self.prices4), self.ev4)



