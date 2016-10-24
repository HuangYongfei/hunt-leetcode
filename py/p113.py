#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import

# 113. Path Sum II
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.


# 总结：


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        return self.pathSumHelper(root, sum, [])

    def pathSumHelper(self, root, sum, path):
        if not root:
            return []
        if root.left is None and root.right is None:
            if sum - root.val == 0:
                path.append(root.val)
                return [path]
            else:
                return []
        path.append(root.val)
        return self.pathSumHelper(root.left, sum - root.val, path[:]) + \
                self.pathSumHelper(root.right, sum - root.val, path[:])


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print('ok')

