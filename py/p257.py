#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import

# 257. Binary Tree Paths


# 总结：https://discuss.leetcode.com/topic/57097/4-lines-python-dfs
# 思路：DFS


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = [str(root.val) + "->" + path for path in self.binaryTreePaths(root.left)]
        res += [str(root.val) + "->" + path for path in self.binaryTreePaths(root.right)]
        return res or [str(root.val)]  # if empty return leaf itself

    def binaryTreePaths2(root):
        def binaryTreePathsHelper(root, res, path):
            if not root.left and not root.right:  # leaf
                res.append(path + str(root.val))
            if root.left:
                binaryTreePathsHelper(root.left, res, path + str(root.val) + '->')
            if root.right:
                binaryTreePathsHelper(root.right, res, path + str(root.val) + '->')

        if not root:
            return []
        res = []
        binaryTreePathsHelper(root, res, '')
        return res




import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':

    print('ok')

