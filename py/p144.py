#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import

# 144. Binary Tree Preorder Traversal

# 总结：


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stk = []
        res = []
        node = root
        while node or stk:
            if node:
                # 访问节点
                res.append(node.val)
                stk.append(node)
                node = node.left
            else:
                node = stk.pop()
                node = node.right
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

