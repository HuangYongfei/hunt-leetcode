#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 总结：
# 1. 暴力解法。逐个扫描
# 2. KMP
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        n1 = len(needle)

        if n1 == 0:
            return 0
        if n < n1:
            return -1

        for x in range(n - n1 + 1):
            flag = True
            for y in range(n1):
                if haystack[x+y] != needle[y]:
                    flag = False
                    break
            if flag:
                return x
        return -1

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().strStr("haystack", "needle")
    print Solution().strStr("haystack", "hay")
    print Solution().strStr("haystack", "stack")
    print Solution().strStr("haystack", "")
    print Solution().strStr("mississippi", "a")
    print Solution().strStr("", "")

    print 'ok'

