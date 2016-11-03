#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import

# 199. Binary Tree Right Side View
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.


# 总结：https://discuss.leetcode.com/topic/16164/5-9-lines-python-48-ms


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        level = [root]
        res = []
        while root and level:
            res.append(level[-1].val)
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return res


    def rightSideView2(self, root):
        # DFS-traverse 深度遍历右子树，然后左子树，每次遇到该深度下的第一个节点记录到数组
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth+1)
                collect(node.left, depth+1)
        view = []
        collect(root, 0)
        return view


    def rightSideView(self, root):
        # 分别计算左右子树的rightSideView，然后组合之
        if not root:
            return []
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        return [root.val] + right + left[len(right):]



import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print('ok')

