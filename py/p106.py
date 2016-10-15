#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import

# 106. Construct Binary Tree from Inorder and Postorder Traversal

# 总结：相关 p105
# <1>已知二叉树的前序序列和中序序列，求解树。
# 1、确定树的根节点。树根是当前树中所有元素在前序遍历中最先出现的元素。
# 2、求解树的子树。找出根节点在中序遍历中的位置，根左边的所有元素就是左子树，根右边的所有元素就是右子树。若根节点左边或右边为空，则该方向子树为空；若根节点边和右边都为空，则根节点已经为叶子节点。
# 3、递归求解树。将左子树和右子树分别看成一棵二叉树，重复1、2、3步，直到所有的节点完成定位。

# <2>、已知二叉树的后序序列和中序序列，求解树。
# 1、确定树的根。树根是当前树中所有元素在后序遍历中最后出现的元素。
# 2、求解树的子树。找出根节点在中序遍历中的位置，根左边的所有元素就是左子树，根右边的所有元素就是右子树。若根节点左边或右边为空，则该方向子树为空；若根节点边和右边都为空，则根节点已经为叶子节点。
# 3、递归求解树。将左子树和右子树分别看成一棵二叉树，重复1、2、3步，直到所有的节点完成定位。


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            # 1. 确定根节点
            root_idx = inorder.index(postorder.pop())
            root = TreeNode(inorder[root_idx])
            # 2. 求解左右子树
            root.left = self.buildTree(inorder[0:root_idx], postorder)
            root.right = self.buildTree(inorder[root_idx+1:], postorder)
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

