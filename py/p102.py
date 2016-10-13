#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import

# 102. Binary Tree Level Order Traversal

# 总结：
# 层次遍历： BFS，借用队列
# 同 p107


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        import collections
        res = []
        if not root:
            return res

        q = collections.deque()
        q.append(root)
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level[:])
        return res

    # https://discuss.leetcode.com/topic/26402/5-6-lines-fast-python-solution-48-ms
    def levelOrder2(self, root):
        # level is a list of the nodes in the current level.
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [child for node in level for child in (node.left, node.right) if child]
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

