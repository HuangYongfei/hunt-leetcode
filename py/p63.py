#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 63. Unique Paths II
# Follow up for "Unique Paths":
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# 总结：相关问题p62
# 动态规划DP问题（与LCS很类似）
# 1. 递归问题f(m, n) = f(m-1, n) + f(m, n-1)
# 2. 使用memo记录中间的子问题的解
# 3. 如果在obstacleGrid(m, n)为1，那么memo(m, n) = 0
# 参考：https://discuss.leetcode.com/topic/4325/my-c-dp-solution-very-simple
#      https://discuss.leetcode.com/topic/10974/short-java-solution

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # https://discuss.leetcode.com/topic/4325/my-c-dp-solution-very-simple
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = [[0] * (n + 1) for _ in range(m + 1)]
        # Nice pre-processing dp[0][1] = 1; to make the code so simple!
        res[0][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1] == 0:
                    res[i][j] = res[i-1][j] + res[i][j-1]

        return res[m][n]

    def uniquePathsWithObstacles2(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if m == 0 or n == 0 or obstacleGrid[0][0] == 1:
            return 0

        res = [[0] * n for _ in range(m)]
        res[0][0] = 1

        for i in range(1, m):
            if obstacleGrid[i][0] == 1 or res[i-1][0] == 0:
                res[i][0] = 0
            else:
                res[i][0] = 1

        for j in range(1, n):
            if obstacleGrid[0][j] == 1 or res[0][j-1] == 0:
                res[0][j] = 0
            else:
                res[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    res[i][j] = res[i-1][j] + res[i][j-1]

        return res[m-1][n-1]


    def uniquePathsWithObstaclesOptSpace(self, obstacleGrid):
        # https://discuss.leetcode.com/topic/10974/short-java-solution
        # 由于计算res[i][j]只需要用到res[i-1]和res[i]行
        # 因此memo只需要min(m,n)，这里直接选取n
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        res = [0] * n
        res[0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    res[j] = 0
                elif j > 0:
                    res[j] = res[j-1] + res[j]

        return res[-1]


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
    print Solution().uniquePathsWithObstacles([[0]])
    print Solution().uniquePathsWithObstacles([[1]])
    print Solution().uniquePathsWithObstacles2([[0,0,0],[0,1,0],[0,0,0]])
    print Solution().uniquePathsWithObstacles2([[1]])
    print Solution().uniquePathsWithObstacles2([[0]])
    print Solution().uniquePathsWithObstaclesOptSpace([[0,0,0],[0,1,0],[0,0,0]])
    print Solution().uniquePathsWithObstaclesOptSpace([[0]])
    print Solution().uniquePathsWithObstaclesOptSpace([[1]])
    print 'ok'

