#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 69. Sqrt(x)
# Implement int sqrt(int x).

# 总结：
#

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        while left <= right:
            mid = (left + right) / 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            if mid ** 2 > x:
                right = mid - 1s
            else:
                left = mid + 1




import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print 'ok'

