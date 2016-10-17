#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import

# 108. Convert Sorted Array to Binary Search Tree


# 总结：
# 对比其他语言的(如C++)，可以发现python简洁的地方就是不在需要设置上下界
# 直接通过切片实现(不过这回带来空间的损耗)，同时不需要关注类型，指针，引用等


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        n = len(nums)
        mid = n // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


    def sortedArrayToBST2(self, nums):
        def dfs(nums, start, end):
            if start <= end:
                mid = start + (end - start) // 2
                root = TreeNode(nums[mid])
                root.left = dfs(nums, start, mid - 1)
                root.right = dfs(nums, mid + 1, end)
                return root
            return None

        if not nums:
            return None
        return dfs(nums, 0, len(nums) - 1)


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print('ok')

