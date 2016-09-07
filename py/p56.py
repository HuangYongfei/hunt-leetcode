#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 56. Merge Intervals
# Given a collection of intervals, merge all overlapping intervals.

# 总结：
#

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[%s, %s]' % (self.start, self.end)

    def __expr__(self):
        return '[%s, %s]' % (self.start, self.end)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        intervals = sorted(intervals, key=lambda x: x.start)

        for x in intervals:
            if res and res[-1].end >= x.start:
                if res[-1].end < x.end:
                    res[-1].end = x.end
            else:
                res.append(x)

        return res



import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    Solution().merge([])
    Solution().merge([Interval(1, 3),Interval(2,6),Interval(8,10),Interval(15,18)])
    print 'ok'

