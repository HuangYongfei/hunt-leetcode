#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 43. Multiply Strings
# Given two numbers represented as strings, return multiplication of the numbers as a string.

# 总结：
# 1. 将字符串转换为数组
# 2. 乘法运算的关系为：res[i+j] = nums[i] * nums[j]

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1, n2 = len(num1), len(num2)
        res = [0] * (n1 + n2)
        # 字符串反转并转为整数列表
        num1 = [int(i) for i in num1][::-1]
        num2 = [int(i) for i in num2][::-1]
        for i in range(n1):
            for j in range(n2):
                res[i+j] += num1[i] * num2[j]

        # 计算进位
        for i in range(len(res)-1):
            res[i+1] += res[i] / 10
            res[i] %= 10

        # 结果转为字符串
        for i in range(len(res)-1, -1, -1):
            if res[i] != 0:
                return ''.join([str(i) for i in reversed(res[:i + 1])])

        return '0'

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().multiply('0', '0')
    print Solution().multiply('123', '23')
    print Solution().multiply('123', '456')
    print 'ok'

