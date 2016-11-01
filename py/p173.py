#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import

# 173. Binary Search Tree Iterator
# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
# Calling next() will return the next smallest number in the BST.
# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.


# 总结：https://discuss.leetcode.com/topic/6575/my-solutions-in-3-languages-with-stack


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # use Stack to store directed left children from root.
        self.stk = list()
        self.pushAll(root)


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stk


    def next(self):
        """
        :rtype: int
        """
        node = self.stk.pop()
        self.pushAll(node.right)
        return node.val


    def pushAll(self, node):
        while node is not None:
            self.stk.append(node)
            node = node.left


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print('ok')

