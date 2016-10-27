#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import

# 129. Sum Root to Leaf Numbers


# 总结：


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        path = []
        self.sumLeafNumbersHelper(root, num, path)
        return sum(path)


    def sumLeafNumbersHelper(self, root, num, path):
        # leaf
        if root and root.left is None and root.right is None:
            path.append(num * 10 + root.val)

        if root.left:
            self.sumLeafNumbersHelper(root.left, num * 10 + root.val, path)
        if root.right:
            self.sumLeafNumbersHelper(root.right, num * 10 + root.val, path)



import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print('ok')

