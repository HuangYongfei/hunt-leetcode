#!/usr/bin/env python
# -*- coding: utf8 -*-

# 109. Convert Sorted List to Binary Search Tree
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.

# 总结：
# relates to: p108, p143
# 参考:
# https://discuss.leetcode.com/topic/18935/python-solutions-convert-to-array-first-top-down-approach-bottom-up-approach


# Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # 转出数组
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        # 同 p108
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


def gen_list(arr):
    head = None
    prev = None
    for x in arr:
        node = ListNode(x)
        if not head:
            prev = head = node
        else:
            prev.next = node
            prev = prev.next
    return head


def disp_list(l):
    while(l):
        print l.val
        l = l.next

if __name__ == '__main__':
    print 'ok'
    a = gen_list([2, 4, 3])
    b = gen_list([5, 6, 4])
    disp_list(a)
    disp_list(b)
    c = Solution().addTwoNumbers(a, b)
    disp_list(c)
