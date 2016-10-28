#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# 143. Reorder List
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# You must do this in-place without altering the nodes' values.
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # 将链表分成两部分
        # find the mid point
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 链表反转参考
        # reverse the second half in-place
        pre, node = None, slow
        while node:
            pre, node.next, node = node, pre, node.next

        # Merge in-place; Note : the last node of "first" and "second" are the same
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next


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
    disp_list(Solution().removeNthFromEnd(gen_list([1, 2, 3, 4, 5]), 2))
    disp_list(Solution().removeNthFromEnd(gen_list([1, 2, 3, 4, 5]), 1))
    disp_list(Solution().removeNthFromEnd(gen_list([1, 2, 3, 4, 5]), 5))
    disp_list(Solution().removeNthFromEnd(gen_list([1, 2, 3, 4, 5]), 8))
    disp_list(Solution().removeNthFromEnd(gen_list([1, 2]), 1))
    disp_list(Solution().removeNthFromEnd(gen_list([1, 2]), 2))

    disp_list(Solution().removeNthFromEnd(gen_list([1]), 1))
    disp_list(Solution().removeNthFromEnd(gen_list([]), 1))


    # disp_list(Solution().removeNthFromEndWithDummy(gen_list([1]), 8))

    print('ok')

