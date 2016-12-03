#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from __future__ import print_function, unicode_literals, absolute_import

# 137. Single Number II
# Given an array of integers, every element appears three times except for one. Find that single one.

# 总结：
#


class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = set(nums)
        res = sum(res) * 3 - sum(nums)
        return res // 2

    def singleNumber2(self, nums):
        res = 0
        for i in range(32):
            count = 0
            # 将每个整数的第 i 为相加
            for num in nums:
                count += (num >> i) & 1
            rem = count % 3
            if i == 31 and rem:
                res -= 1 << 31
            else:
                res |= rem * (1 << i)
        return res

import unittest


class TestSolution(unittest.TestCase):

    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print('ok')
