#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from __future__ import print_function, unicode_literals, absolute_import

# 136. Single Number
# Given an array of integers, every element appears twice except for one. Find that single one.

# 总结：
#


class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(operator.xor, nums)

import unittest


class TestSolution(unittest.TestCase):

    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print('ok')
