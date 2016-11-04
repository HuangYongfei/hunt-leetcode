#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# 203. Remove Linked List Elements
# Remove all elements from a linked list of integers that have value val.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        p1 = p2 = dummy
        while p1:
            while p1 and p1.val != val:
                p2, p1 = p1, p1.next
            if p1 and p1.val == val:
                p2.next = p1.next
                p1 = p1.next

        return dummy.next

    # 删除链表节点: 需要注意区分删除头结点和其他节点(中间节点和尾节点无区别)
    # 这里: Use dummy node to get rid of the trouble of head.
    def removeElements2(self, head, val):
        dummy = ListNode(None)
        dummy.next = head
        p = dummy
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next

        return dummy.next

    # 尾递归解法及其循环解法
    # https://discuss.leetcode.com/topic/19529/simple-and-elegant-solution-in-c


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
        s = "%s -> " % l.val
        print(s, end='')
        l = l.next
    print('\n')

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print(disp_list(Solution().removeElements(gen_list([1]), 1)))
    print(disp_list(Solution().removeElements(gen_list([1,2,6,3,4,5,6]), 6)))
    print('ok')

