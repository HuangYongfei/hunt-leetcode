#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 62. Unique Paths
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?

# 总结：
# 动态规划DP问题（与LCS很类似）
# 1. 递归问题f(m, n) = f(m-1, n) + f(m, n-1)
# 2. 使用memo记录中间的子问题的解

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    res[i][j] = 1
                else:
                    res[i][j] = res[i-1][j] + res[i][j-1]

        return res[m-1][n-1]


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().uniquePaths(1, 2)
    print 'ok'

