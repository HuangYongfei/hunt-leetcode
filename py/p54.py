#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 54. Spiral Matrix
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# 总结：
# 思路一：
# 1. 上右下左（可能左不存在）构成一圈，通过cirs = min(m // 2, n // 2)确定一圈的次数
# 2. 循环cirs次，将完整的一圈的次数依次添加到res中
# 3. 将不能构成一圈（至少有上或右）
# 4. p.s. 实现过程中利用python的range在start>=end的时候没有循环，省去了一些判断

# 思路二：
# https://discuss.leetcode.com/topic/15558/a-concise-c-implementation-based-on-directions
# 1. 发现如果将向右和向左（水平），向下和向上（竖直）移动的次数合起来看，可以发现在
#    水平和竖直方向上移动的步数上是连续的，直到其中一个为0退出
# 2. 引入方向数组dirs和index_dir来移动下标
# 3. 引入steps数组来作为水平和竖直方向上移动步数的记录
# 4. p.s. 比如：
# 0 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 水平方向为：5(right)，4(left)，3(left)
# 竖直方向为：2(down)，1(up)，0(quit)
# 水平或竖直为0后退出


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        m = len(matrix)
        if m == 0:
            return res

        n = len(matrix[0])
        if n == 0:
            return res

        # 可以构成一圈的次数
        cirs = min(m // 2, n // 2)
        for i in range(0, cirs):
            # 上
            # [x][i:n-i]
            for j in range(i, n - i):
                # print matrix[i][j]
                res.append(matrix[i][j])

            # 右
            # 不包括[i][x], 从i+1开始
            # [i+1:m-i][x]
            for j in range(i+1, m - i):
                # print matrix[j][n-1-i]
                res.append(matrix[j][n-1-i])

            # 下
            # 不包括[x][n-1-i], 从[x][n-1-i-1]开始，到i
            # [x][n-1-i-1:i-1]
            for j in range(n-1-i-1, i-1, -1):
                # print matrix[m-1-i][j]
                res.append(matrix[m-1-i][j])

            # 左
            # 不包括[m-1-i][x] 和 [i][x]
            # [m-1-i-1:i][x]
            for j in range(m-1-i-1, i, -1):
                # print matrix[j][i]
                res.append(matrix[j][i])

        # 不能构成一圈的数
        if min(m,n) - cirs * 2:
            # 上
            # print 'cirs: ', cirs
            for j in range(cirs, n - cirs):
                # print matrix[cirs][j]
                res.append(matrix[cirs][j])

            # 右
            for j in range(cirs+1, m - cirs):
                res.append(matrix[j][n-1-cirs])

        return res

    def spiralOrder2(self, matrix):
        res = []
        m = len(matrix)
        if m == 0:
            return res

        n = len(matrix[0])
        if n == 0:
            return res

        # right, down, left, up，分别代表x，y坐标的移动
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # y(right,left), x(down,up)方向移动的初始次数：n, m-1
        steps = [n, m - 1]
        index_dir = 0  # index of direction
        i_r = 0  # initial position
        i_c = -1

        # steps[index%2]分别得到(right,left), (down,up)方向移动的次数
        while steps[index_dir%2]:
            for k in range(steps[index_dir%2]):
                i_r += dirs[index_dir][0]
                i_c += dirs[index_dir][1]
                res.append(matrix[i_r][i_c])

            # y(right,left), x(down,up)方向移动的次数减一
            steps[index_dir%2] -= 1
            # 改变方向
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
    print Solution().spiralOrder([
                                 [ 1, 2, 3 ],
                                 [ 4, 5, 6 ],
                                 [ 7, 8, 9 ]
                                ])
    print Solution().spiralOrder([
                                 [ 1, 2, 3 ],
                                 [ 4, 5, 6 ]
                                ])
    print Solution().spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
    print Solution().spiralOrder([[1,2,3,4,5,6,7,8,9,10]])

    print '==solutin2=='
    print Solution().spiralOrder2([
                                 [ 1, 2, 3 ],
                                 [ 4, 5, 6 ],
                                 [ 7, 8, 9 ]
                                ])
    print Solution().spiralOrder2([
                                 [ 1, 2, 3 ],
                                 [ 4, 5, 6 ]
                                ])
    print Solution().spiralOrder2([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
    print Solution().spiralOrder2([[1,2,3,4,5,6,7,8,9,10]])
    print 'ok'

