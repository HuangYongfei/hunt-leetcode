#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 64. Minimum Path Sum
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path
# Note: You can only move either down or right at any point in time.

# 总结：
# 1. DP算法。相关问题: p62, p63, p64

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        res = [ [2147483647] * n for _ in range(m)]
        res[0][0] = grid[0][0]
        for i in range(1, m):
            res[i][0] = grid[i][0] + res[i-1][0]
        for j in range(1, n):
            res[0][j] = grid[0][j] + res[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                temp = min(res[i-1][j], res[i][j-1])
                res[i][j] = min(res[i][j], temp + grid[i][j])
        print res
        return res[-1][-1]

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().minPathSum([[0]])
    print Solution().minPathSum([[1,2], [3, 4]])
    print Solution().minPathSum([[1,2], [1, 1]])
    print Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]])
    print 'ok'

