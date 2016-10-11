#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import

# 95. Unique Binary Search Trees II
# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

# 总结：
#


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # https://discuss.leetcode.com/topic/15886/should-be-6-liner
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate(first, last):
            trees = []
            for root in range(first, last+1):
                for left in generate(first, root-1):
                    for right in generate(root+1, last):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)

            return trees or [None]

        def generate_list(first, last):
            def conn_node(val, left, right):
                node = TreeNode(val)
                node.left = left
                node.right = right
                return node

            return [ conn_node(root, left, right)
                for root in range(first, last+1)
                for left in generate_list(first, root-1)
                for right in generate_list(root+1, last)
                ] or [None]


        if n == 0:
            return []
        return generate(1, n)



import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print(Solution().generateTrees(0))
    print('ok')

