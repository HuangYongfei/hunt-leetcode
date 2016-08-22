#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        r_s = []
        for i in range(len(strs[0])):
            common_flag = True
            for j in range(1, len(strs)):
                if i >= len(strs[j]):
                    common_flag = False
                    break
                if strs[0][i] != strs[j][i]:
                    common_flag = False
                    break
            if common_flag:
                r_s.append(strs[0][i])
            else:
                break
        return ''.join(r_s)

    def longestCommonPrefixOpt(self, strs):
        if len(strs) == 0:
            return ''

        r_s = []
        sorted_strs = sorted(strs)
        s1 = sorted_strs[0]
        s2 = sorted_strs[len(sorted_strs) - 1]
        for i in range(len(s1)):
            if len(s2) > i and s2[i] == s1[i]:
                r_s.append(s1[i])
            else:
                return ''.join(r_s)
        return ''.join(r_s)


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(Solution().longestCommonPrefix(['abc']), 'abc')
        self.assertEqual(Solution().longestCommonPrefix([]), '')
        self.assertEqual(Solution().longestCommonPrefix(['abc', 'ab', 'a']), 'a')
        self.assertEqual(Solution().longestCommonPrefix(['abc', 'ab', 'ab']), 'ab')
        self.assertEqual(Solution().longestCommonPrefix(['abcd', 'adb', 'adb']), 'a')

        self.assertEqual(Solution().longestCommonPrefixOpt(['abc']), 'abc')
        self.assertEqual(Solution().longestCommonPrefixOpt([]), '')
        self.assertEqual(Solution().longestCommonPrefixOpt(['abc', 'ab', 'a']), 'a')
        self.assertEqual(Solution().longestCommonPrefixOpt(['abc', 'ab', 'ab']), 'ab')
        self.assertEqual(Solution().longestCommonPrefixOpt(['abcd', 'adb', 'adb']), 'a')

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print 'ok'

