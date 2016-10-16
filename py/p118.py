#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import


# 118. Pascal's Triangle
# Given numRows, generate the first numRows of Pascal's triangle.

# 总结：
#


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        res = [[1]]
        path = [1]
        for _ in range(1, numRows):
            temp = [1]
            for i in range(0, len(path)-1):
                temp.append(path[i]+path[i+1])
            temp.append(1)
            res.append(temp[:])
            path = temp[:]
        return res

    def generate2(self, numRows):
        # Any row can be constructed using the offset sum of the previous row.
        #    1 3 3 1 0
        # +  0 1 3 3 1
        # =  1 4 6 4 1
        # https://discuss.leetcode.com/topic/22628/python-4-lines-short-solution-using-map

        if numRows == 0:
            return []
        row = [1]
        res = [[1]]
        for i in range(0, numRows - 1):
            res.append([l + r for l, r in zip(res[-1] + [0], [0] + res[-1])])
        return res




import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    # print(Solution().generate(5))
    print(Solution().generate2(5))
    print('ok')

