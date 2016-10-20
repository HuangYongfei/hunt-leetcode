#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import


# 120. Triangle
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# 总结：
# 参考：
# 1. https://discuss.leetcode.com/topic/1669/dp-solution-for-triangle
# 2. https://discuss.leetcode.com/topic/13970/one-liner-in-python
# 3. https://discuss.leetcode.com/topic/19754/python-easy-to-understand-solutions-top-down-bottom-up


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # https://discuss.leetcode.com/topic/1669/dp-solution-for-triangle
        # bottom-up dp: we start from the nodes on the bottom row; the min pathsums for these nodes are the values of the nodes themselves. From there, the min pathsum at the ith node on the kth row would be the lesser of the pathsums of its two children plus the value of itself,
        # i.e.:
        # minpath[k][i] = min( minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i];
        # Or even better, since the row minpath[k+1] would be useless after minpath[k] is computed, we can simply set minpath as a 1D array, and iteratively update itself:

        # For the kth level:
        # minpath[i] = min( minpath[i], minpath[i+1]) + triangle[k][i];

        dp = triangle[-1][:]
        n = len(triangle)
        for layer in range(n-2, -1, -1):  # for each layer
            for j in range(layer+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[layer][j]

        return dp[0]

    # https://discuss.leetcode.com/topic/13970/one-liner-in-python
    def minimumTotalOneLine(self, triangle):
        return reduce(lambda acc, x: [upper + min(lower1, lower2) for upper, lower1, lower2 in zip(x, acc, acc[1:])], triangle[::-1])[0]



import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print('ok')

