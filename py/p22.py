#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        s = ''
        res = []
        self.recur(res, n, n, s)
        return res

    def recur(self, res, left, right, s):
        if (left, right) == (0, 0):
            res.append(s)
        if left > 0:
            self.recur(res, left - 1, right, s + '(')
        if left < right:
            self.recur(res, left, right - 1, s + ')')

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print 'ok'

