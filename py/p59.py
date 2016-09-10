#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 59. Spiral Matrix II
# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# 总结：
# p54

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # init matrix
        # res = [[0] * n] * n # shallow copies
        # 正确创建多维数组的方式
        res = [[0] * n for i in range(n)]


        # right, down, left, up，分别代表x，y坐标的移动
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # index of direction
        index_dir = 0
        # init steps, y(right,left), x(down,up)方向移动的初始次数：n, m-1
        steps = [n, n - 1]
        # index of row, index of col
        i_r, i_c = 0, -1

        count = 0
        while steps[index_dir%2]:
            for k in range(steps[index_dir%2]):
                i_r += dirs[index_dir][0]
                i_c += dirs[index_dir][1]
                count += 1
                res[i_r][i_c] = count

            # y(right,left), x(down,up)方向移动的次数减一
            steps[index_dir%2] -= 1
            index_dir = (index_dir + 1) % 4

        return res

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':

    print Solution().generateMatrix(3)
    print Solution().generateMatrix(0)
    print Solution().generateMatrix(2)
    print 'ok'

