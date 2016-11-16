#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from __future__ import print_function, unicode_literals, absolute_import

# 103. Binary Tree Zigzag Level Order Traversal
# Given a binary tree, return the zigzag level order traversal of its
# nodes' values. (ie, from left to right, then right to left for the next
# level and alternate between).

# 总结：
# 层次遍历： BFS，借用队列
# 同 p107, p102


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans, level = [], [root]
        left_to_right = True
        while root and level:
            if left_to_right:
                ans.append([node.val for node in level])
            else:
                ans.append([node.val for node in level[::-1]])

            left_to_right = not left_to_right
            level = [child for node in level for child in (
                node.left, node.right) if child]

        return ans

import unittest


class TestSolution(unittest.TestCase):

    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print('ok')
