#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import


# 119. Pascal's Triangle II
# Given an index k, return the kth row of the Pascal's triangle.

# 总结：
#


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        path = [1]
        for _ in range(1, rowIndex+1):
            path = [1] + [path[i] + path[i+1] for i in range(0, len(path)-1)] + [1]

        return path

    def getRow2(self, rowIndex):
        # Any row can be constructed using the offset sum of the previous row.
        #    1 3 3 1 0
        # +  0 1 3 3 1
        # =  1 4 6 4 1
        # https://discuss.leetcode.com/topic/22628/python-4-lines-short-solution-using-map

        row = [1]
        for i in range(0, rowIndex):
            row = [l + r for l, r in zip(row + [0], [0] + row)]
        return row




import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print(Solution().getRow(0))
    print(Solution().getRow(3))
    print(Solution().getRow2(0))
    print(Solution().getRow2(3))
    # print(Solution().generate2(5))
    print('ok')

