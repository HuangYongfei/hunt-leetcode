#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 74. Search a 2D Matrix
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# 总结：
#


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        column = len(matrix[0])
        while left <= right:
            mid = (right + left)/2
            i = mid / column
            j = mid % column
            if (matrix[i][j] == target):
                return True
            elif (matrix[i][j] < target):
                left = mid + 1
            else:
                right = mid - 1
        return False


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print 'ok'

