#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 总结:
# 1. 负数返回False
# 2. 思路：根据原数x的低位到高位构建一个新的数y，比较x和y是否相等

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x1 = x
        y = 0
        while x1:
            y = y * 10 + x1 % 10
            x1 = x1 / 10
        if y == x:
            return True
        return False

import unittest
class TestSolution(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(Solution().isPalindrome(1))
        self.assertFalse(Solution().isPalindrome(-1))
        self.assertFalse(Solution().isPalindrome(123))
        self.assertTrue(Solution().isPalindrome(121))
        self.assertTrue(Solution().isPalindrome(111))

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print 'ok'