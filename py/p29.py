#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 总结：
# 1. 利用除数翻倍
# 参考：https://discuss.leetcode.com/topic/6966/15-line-easy-understand-solution-129ms
# for example, if we want to calc (17/2)
# ret = 0;
# 17-2 ,ret+=1; left=15
# 15-4 ,ret+=2; left=11
# 11-8 ,ret+=4; left=3
# 3-2 ,ret+=1; left=1
# ret=8;

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return -1

        sign_flag = 0
        if dividend >= 0 and divisor < 0 or dividend <= 0 and divisor > 0:
            sign_flag = 1

        divisor = abs(divisor)
        dividend = abs(dividend)
        res = 0
        sub = divisor
        step = 1
        while dividend >= divisor:
            if dividend >= sub:
                dividend -= sub
                res += step
                sub = sub << 1
                step = step << 1
            else:
                sub = sub >> 1
                step = step >> 1

        if sign_flag:
            res = -res
        return min(max(-2147483648, res), 2147483647)

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print 'ok'

