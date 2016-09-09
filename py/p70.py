#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 70. Climbing Stairs
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# 总结：
# 斐波那契数列


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n
        f1, f2 = 1, 2
        res = 0
        for i in range(3, n+1):
            res = f1 + f2
            f1 = f2
            f2 = res

        return res

    def climbStairs2(self, n):
        f1, f2 = 0, 1
        for _ in range(n):
            f1, f2 = f2, f1 + f2

        return f2


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().climbStairs(1)
    print Solution().climbStairs(2)
    print Solution().climbStairs(3)
    print Solution().climbStairs(4)
    print Solution().climbStairs(5)

    print Solution().climbStairs2(1)
    print Solution().climbStairs2(2)
    print Solution().climbStairs2(3)
    print Solution().climbStairs2(4)
    print Solution().climbStairs2(5)
    print 'ok'

