"""
Type: heaps, sorting
Source: Leetcode (Medium)
Prompt: Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Examples:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Input: [[7,10],[2,4]]
Output: 1

Parameters:
- intervals: Interval object

Returns: int
"""

import unittest
import heapq

class Interval:

	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

def meeting_rooms(intervals):
	''' Sorts by type and time.
	t: O(nlogn)
	s: O(n)
	'''
	starts = sorted([i.start for i in intervals])
	ends = sorted([i.end for i in intervals])
	alloc, occup, s, e = 0, 0, 0, 0

	while s < len(starts):
		if starts[s] < ends[e]:
			if alloc == occup:
				alloc += 1
			occup += 1
			s += 1
		else:
			occup -= 1
			e += 1

	return alloc

def meeting_rooms_heap(intervals):
	''' Uses a min-heap.
	t: O(nlogn)
	s: O(n)
	'''
	if not intervals:
		return 0

	intervals.sort(key=lambda x: x.start)
	rooms = []
	heapq.heappush(rooms, intervals[0].end)
	for i in intervals[1:]:
		if i.start >= rooms[0]:
			heapq.heappop(rooms)
		heapq.heappush(rooms, i.end)

	return len(rooms)


class MeetingRoomsTests(unittest.TestCase):

	def setUp(self):
		self.intervals1 = [Interval(s=0, e=30), Interval(s=5, e=10), Interval(s=15, e=20)]
		self.ev1 = 2
		self.intervals2 = [Interval(s=7, e=10), Interval(s=2, e=4)]
		self.ev2 = 1
		self.intervals3 = [Interval(s=1, e=10), Interval(s=2, e=7), Interval(s=3, e=19), Interval(s=8, e=12), Interval(s=10, e=20), Interval(s=11, e=30)]
		self.ev3 = 4
		self.intervals4 = []
		self.ev4 = 0

	def test_meeting_rooms(self):
		self.assertEqual(meeting_rooms(self.intervals1), self.ev1)
		self.assertEqual(meeting_rooms(self.intervals2), self.ev2)
		self.assertEqual(meeting_rooms(self.intervals3), self.ev3)
		self.assertEqual(meeting_rooms(self.intervals4), self.ev4)

	def test_meeting_rooms_heap(self):
		self.assertEqual(meeting_rooms_heap(self.intervals1), self.ev1)
		self.assertEqual(meeting_rooms_heap(self.intervals2), self.ev2)
		self.assertEqual(meeting_rooms_heap(self.intervals3), self.ev3)
		self.assertEqual(meeting_rooms_heap(self.intervals4), self.ev4)


if __name__ == '__main__':
	unittest.main()