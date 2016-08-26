#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        r_s = []
        pair_d = {'}': '{',']': '[', ')': '('}
        for ch in s:
            if ch in ('{', '[', '('):
                r_s.append(ch)
            elif ch in ('}', ']', ')'):
                if not r_s:
                    return False
                if pair_d[ch] != r_s[-1]:
                    return False
                r_s.pop()
        if r_s:
            return False
        return True

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().isValid('()')
    print Solution().isValid('()[]{}')
    print Solution().isValid('(]')
    print Solution().isValid('([)]')
    print 'ok'

