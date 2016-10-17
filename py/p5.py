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
                # j - i < 3: first initialize the one and two letters palindromes
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i+1][j-1])

                if dp[i][j] and (not res or j - i + 1 > len(res)):
                    res = s[i:j+1]

        return res

    # https://leetcode.com/articles/longest-palindromic-substring/
    def longestPalindrome2(self, s):
        def expandAroundCenter(s, left, right):
            l, r, n = left, right, len(s)
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1


        start = end = 0
        for i in range(len(s)):
            l1 = expandAroundCenter(s, i, i)
            l2 = expandAroundCenter(s, i, i+1)
            l = max(l1, l2)
            if l > end - start:
                start = i - (l - 1) // 2
                end = i + l // 2

        return s[start:end+1]



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
    print(Solution().longestPalindrome2('abc'))
    print(Solution().longestPalindrome2('abba'))
    print(Solution().longestPalindrome2('abbaccab'))
    print('ok')

