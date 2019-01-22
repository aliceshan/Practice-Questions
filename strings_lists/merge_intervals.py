"""
Type: lists
Source: Leetcode (Medium)
Prompt: Given a collection of intervals, merge all overlapping intervals.

Examples:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Parameters:
- intervals: list of Intervals

Returns: list of Intervals
"""

import unittest
import heapq

class Interval:
	def __init__(self, start, end):
		self.start = start
		self.end = end


def merge_intervals(intervals):
	''' Sorting and list iteration.
	t: O(nlogn) - sort time
	s: O(n) - constant if we can sort intervals in place
	'''
	output = []
	for i in sorted(intervals, key=lambda x: x.start):
		if not output or output[-1].end < i.start:
			output.append(i)
		else:
			output[-1].end = max(output[-1].end, i.end)

	return output


def merge_intervals_heap(intervals):
	''' Using a heap
	t: O(nlogn)
	s: O(n)
	'''
	output = []
	h = []
	for i in intervals:
		heapq.heappush(h, (i.start, 0))
		heapq.heappush(h, (i.end, 1))

	while h:
		start = heapq.heappop(h)[0]
		count = 1
		while count > 0:
			end, val = heapq.heappop(h)
			count = count+1 if val == 0 else count-1
		output.append(Interval(start, end))

	return output


class MergeIntervalsTests(unittest.TestCase):

	def setUp(self):
		self.intervals1 = [Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)]
		self.ev1 = [Interval(1,6),Interval(8,10),Interval(15,18)]
		self.intervals2 = [Interval(1,4),Interval(4,5),Interval(6,6)]
		self.ev2 = [Interval(1,5),Interval(6,6)]
		self.intervals3 = []
		self.ev3 = []

	def test_merge_intervals(self):
		self.assertEqual([(i.start,i.end) for i in merge_intervals(self.intervals1)], [(i.start,i.end) for i in self.ev1])
		self.assertEqual([(i.start,i.end) for i in merge_intervals(self.intervals2)], [(i.start,i.end) for i in self.ev2])
		self.assertEqual([(i.start,i.end) for i in merge_intervals(self.intervals3)], [(i.start,i.end) for i in self.ev3])

	def test_merge_intervals_heap(self):
		self.assertEqual([(i.start,i.end) for i in merge_intervals_heap(self.intervals1)], [(i.start,i.end) for i in self.ev1])
		self.assertEqual([(i.start,i.end) for i in merge_intervals_heap(self.intervals2)], [(i.start,i.end) for i in self.ev2])
		self.assertEqual([(i.start,i.end) for i in merge_intervals_heap(self.intervals3)], [(i.start,i.end) for i in self.ev3])

if __name__ == '__main__':
	unittest.main()
