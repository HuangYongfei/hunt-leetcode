#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import

# 89. Gray Code
# The gray code is a binary numeral system where two successive values differ in only one bit.
# Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2


# 总结：
# 要从连续性去考虑，不能直接从n=2考虑怎么计算，而应该n=2是在n=1的结果dp[1]上在将n=1的结果
# 反向加上2^(n-1)次方得到:
#   dp[n] = dp[n-1].append(reverse(dp[n-1]).each.plus(2^(n-1)))
# n = 0: [0]
# n = 1: [0] + [1+0][::-1] = [0,1]
# n = 2: [0,1] + [2+0, 2+1][::-1] = [0,1,3,2]
# n = 3: [0,1,3,2] + [4 + 0, 4 +1, 4 +3, 4 + 2][::-1] = [0,1,3,2,6,7,5,4]
# 1. https://discuss.leetcode.com/topic/1011/what-is-the-best-solution-for-gray-code-problem-no-extra-space-used-and-no-recursion/3
# 2. 思路和1中的一样的DP版：https://discuss.leetcode.com/topic/58660/dp-python-solution

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(0, n):
            inc = 2 ** i
            for j in range(len(res)-1, -1, -1):
                res.append(res[j] + inc)
            # simplify
            # res += [(x + 2**i) for x in reversed(res)]
        return res

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print(Solution().grayCode(2))
    print('ok')

