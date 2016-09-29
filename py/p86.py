#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# 86. Partition List
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # 将整个链表打断分成两部分：first开头和second开头
        # first开头的链表将所有小于x的元素链接在一起
        # second开头的链表将所有大于等于x的元素连接在一起
        # 最后将first的尾部指向second的头部
        first, second = ListNode(None), ListNode(None)
        first_curr, second_curr = first, second
        curr = head
        # 将链表分段
        while curr:
            if curr.val < x:
                first_curr.next = curr
                curr, first_curr = curr.next, first_curr.next
                first_curr.next = None  # 断开
            else:
                second_curr.next = curr
                curr, second_curr = curr.next, second_curr.next
                second_curr.next = None

        # first的尾部指向second的头部
        first_curr.next = second.next
        return first.next

    # 1. 找出开头处相连的小于x的(t_list)最后一个节点t
    # 2. 从t.next（p）开始，找出接下来相连的大于等于x的（list_p)最后一个节点p
    # 3. 将t和p.next连接，同时p.next指向list_p的开头，list_p的结尾指向p.next.next
    # 4. 循环2，3
    def partition2(self, head, x):
        dummy = ListNode(None)
        dummy.next = head
        t = dummy
        # 1.
        while t.next and t.next.val < x:
            t = t.next
        # 此时t指向开头一串节点中小于x的最后一个节点，p则为>=x的第一个节点或为末尾节点
        p = t.next
        if not p:
            return dummy.next

        # 4.
        while p.next:
            # 2.
            while p.next and p.next.val >= x:
                p = p.next
            # 3.
            if p.next:
                tmp = p.next
                p.next = p.next.next
                tmp.next = t.next
                t.next = tmp
                t = tmp

        return dummy.next

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
    # disp_list(Solution().partition(gen_list([1, 4, 3, 2, 5, 2]), 3))
    # disp_list(Solution().partition(gen_list([1]), 2))
    # disp_list(Solution().partition(gen_list([2, 1]), 2))
    # disp_list(Solution().partition(gen_list([1, 4, 3, 4, 5]), 2))
    # disp_list(Solution().partition(gen_list([3, 4, 2, 2, 1]), 5))
    # disp_list(Solution().partition(gen_list([3, 4, 2, 2, 1]), 2))
    # disp_list(Solution().partition(gen_list([]), 5))

    disp_list(Solution().partition2(gen_list([1, 4, 3, 2, 5, 2]), 3))
    disp_list(Solution().partition2(gen_list([1]), 2))
    disp_list(Solution().partition2(gen_list([2, 1]), 2))
    disp_list(Solution().partition2(gen_list([1, 4, 3, 4, 5]), 2))
    disp_list(Solution().partition2(gen_list([3, 4, 2, 2, 1]), 5))
    disp_list(Solution().partition2(gen_list([3, 4, 2, 2, 1]), 2))
    disp_list(Solution().partition2(gen_list([]), 5))


    print('ok')

