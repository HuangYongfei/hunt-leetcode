#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import

# 110. Balanced Binary Tree


# 总结：


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(root):
            return 0 if not root else max(depth(root.left), depth(root.right)) + 1

        # 叶子
        if not root:
            return True
        # 左右子树高度差
        if abs(depth(root.left) - depth(root.right)) > 1:
            return False
        # 递归求解
        return self.isBalanced(root.left) and self.isBalanced(root.right)


    def isBalanced2(self, root):
        def depth(root):
            if not root:   # leaves
                return 0
            left = depth(root.left) # left child's depth
            right = depth(root.right) # right child's depth
            if abs(left - right) > 1:
                raise Exception('not balanced') # stop recursion
            return max(left, right) + 1

        if not root:
            return True
        try:
            return abs(depth(root.left) - depth(root.right)) <= 1
        except:
            return False





import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print('ok')

