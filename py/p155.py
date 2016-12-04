#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from __future__ import print_function, unicode_literals, absolute_import

# 155. Min Stack


# 总结：
# https://discuss.leetcode.com/topic/11985/my-python-solution

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curr_min = self.getMin()
        if curr_min is None or x < curr_min:
            curr_min = x

        self.stk.append((x, curr_min))

    def pop(self):
        """
        :rtype: void
        """
        self.stk.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stk) == 0:
            return None
        else:
            return self.stk[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stk) == 0:
            return None
        else:
            return self.stk[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

import unittest


class TestSolution(unittest.TestCase):

    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print('ok')
