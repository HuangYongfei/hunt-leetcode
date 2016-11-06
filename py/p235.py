#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import

# 235. Lowest Common Ancestor of a Binary Search Tree


# 总结：https://discuss.leetcode.com/topic/18387/3-lines-with-o-1-space-1-liners-alternatives
# 思路：both p and q are in the same subtree (meaning their values are both smaller or both larger than root's).


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root

    def lowestCommonAncestorBSTRecur(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestorBSTRecur(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestorBSTRecur(root.right, p, q)
        else:
            return root



import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print('ok')

