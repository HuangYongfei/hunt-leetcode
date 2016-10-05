#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import


# 93. Restore IP Addresses
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
# For example:
# Given "25525511135",
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

# 总结：
#

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        path = []
        self.backtrack(s, 0, 0, path, res)
        return res

    def backtrack(self, s, start, depth, path, res):
        if depth == 4 and start == len(s):
            res.append('.'.join(path))
            return res
        if start >= len(s) or depth >= 4:
            return
        for i in range(start, max(start+3, len(s))):
            t = s[start:i+1]
            if t[0] == '0' and t!= '0':
                continue
            if int(t) >= 0 and int(t) <= 255:
                self.backtrack(s, i+1, depth+1, path+[t], res)


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print(Solution().restoreIpAddresses("25525511135"))
    print('ok')

