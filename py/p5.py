#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import

# 5. Longest Palindromic Substring
# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

# 总结：
# 1. DP(https://discuss.leetcode.com/topic/25500/share-my-java-solution-using-dynamic-programming):
#    dp(i, j) represents whether s(i ... j) can form a palindromic substring, dp(i, j) is true when s(i) equals to s(j) and s(i+1 ... j-1) is a palindromic substring. When we found a palindrome, check if it's the longest one. Time complexity O(n^2).




class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) <= 1:
            return s

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = ''

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i+1][j-1])

                if dp[i][j] and (not res or j - i + 1 > len(res)):
                    res = s[i:j+1]

        return res


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print(Solution().longestPalindrome('abc'))
    print(Solution().longestPalindrome('abba'))
    print(Solution().longestPalindrome('abbaccab'))
    print('ok')

