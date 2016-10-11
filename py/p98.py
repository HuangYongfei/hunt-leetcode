#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import

# 98. Validate Binary Search Tree

# 总结：
#


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTHelper(root, None, None)

    # 递归判断子树是否为二叉搜索树，中序遍历
    def isValidBSTHelper(self, root, minNode, maxNode):
        if not root:
            return True
        if (minNode and root.val <= minNode.val) or \
           (maxNode and root.val >= maxNode.val):
            return False
        return self.isValidBSTHelper(root.left, minNode, root) and \
               self.isValidBSTHelper(root.right, root, maxNode)


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print('ok')

