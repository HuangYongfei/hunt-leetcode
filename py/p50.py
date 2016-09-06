#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 50. Pow(x, n)
# Implement pow(x, n).

# 总结：
# 1. 二分法


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        if n < 0:
            n = -n
            x = 1.0 / x
        return self.myPow(x*x, n/2) if n % 2 == 0 else x * self.myPow(x*x, n/2)


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print 'ok'

