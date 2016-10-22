#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import

# 111. Minimum Depth of Binary Tree
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


# 总结：


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if not root:
        #     return 0
        # elif not root.left or not root.right:
        #     return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        # else:
        #     return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

        if not root:
            return 0
        minLeft = self.minDepth(root.left)
        minRight = self.minDepth(root.right)
        if minLeft == 0 or minRight == 0:
            return minLeft + minRight + 1
        else:
            return min(minLeft, minRight) + 1


    def minDepth2(self, root):
        if not root:
            return 0
        depth = 0
        q = []
        q.append(root)
        while q:
            depth += 1  # each level increment the depth
            # 将同一层的节点的子节点入队
            for _ in range(len(q)):
                node = q.pop(0)
                if node and not node.left and not node.right: # 遇到叶子返回最近深度
                    return depth
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return depth



import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print('ok')

