#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# 148. Sort List
# Sort a linked list in O(n log n) time using constant space complexity.



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # p1 move 1 step every time, p2 move 2 step every time, pre record node before p1
        p1 = p2 = pre = head
        while p2 and p2.next:
            pre, p1, p2 = p1, p1.next, p2.next.next

        # change pre next to null, make two sub list(head to pre, p1 to p2)
        pre.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(p1)
        return self.mergeSortedList(l1, l2)

    def mergeSortedList(self, l1, l2):
        dummy = p = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                p.next, p, l1 = l1, l1, l1.next
            else:
                p.next, p, l2 = l2, l2, l2.next

        p.next = p.next = l1 or l2
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

    print('ok')

