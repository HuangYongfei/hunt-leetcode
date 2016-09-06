#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 58. Length of Last Word
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# 总结：
#

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        n = len(s)
        for i in range(n):
            if s[i] != ' ':
                res += 1
            # 新的lastword开始: s[i] == ' ' and s[i+1] != ' '
            elif i + 1 < n and s[i+1] != ' ':
                res = 0

        return res

    def lengthOfLastWord2(self, s):
        # s.split() != s.split(' ')
        return len(s.split()[-1]) if len(s.split()) >= 1 else 0

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().lengthOfLastWord("hello world")
    print Solution().lengthOfLastWord("a ")
    print Solution().lengthOfLastWord("ab  ")
    print Solution().lengthOfLastWord2("hello world")
    print Solution().lengthOfLastWord("a ")
    print 'ok'

