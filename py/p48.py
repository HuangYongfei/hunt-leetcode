#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 48. Rotate Image
# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).

# 总结：
# 1. 先对角线交换
# 2. 然后翻转即可

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(i, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(cols):
            for j in range(rows // 2):
                matrix[i][j], matrix[i][rows-1-j] = matrix[i][rows-1-j], matrix[i][j]

        return matrix



import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().rotate([[1,2],[3,4]]) # [[3,1],[4,2]]
    print Solution().rotate([[1]])  # [[1]]
    print 'ok'

