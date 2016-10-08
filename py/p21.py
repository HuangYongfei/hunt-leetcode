#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        if not l1 or not l2:
            if l1:
                head = l1
                l1 = l1.next
            elif l2:
                head = l2
                l2 = l2.next
            else:
                return []
        else:
            if l1.val <= l2.val:
                head = l1
                l1 = l1.next
            else:
                head = l2
                l2 = l2.next
        prev = head
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                prev = prev.next
                l1 = l1.next
            else:
                prev.next = l2
                prev = prev.next
                l2 = l2.next

        while l1:
            prev.next = l1
            prev = prev.next
            l1 = l1.next

        while l2:
            prev.next = l2
            prev = prev.next
            l2 = l2.next

        return head

    def mergeTwoLists2(self, l1, l2):
        dummy = tail = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, tail, l1 = l1, l1, l1.next
            else:
                tail.next, tail, l2 = l2, l2, l2.next

        tail.next = l1 or l2
        return dummy.next


def gen_list(arr):
    prev = head = None
    for x in arr:
        node = ListNode(x)
        if head:
            prev.next = node
            prev = prev.next
        else:
            prev = head = node
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
    a = gen_list([1, 2, 3 , 4])
    b = gen_list([5, 6, 7, 8])
    disp_list(Solution().mergeTwoLists(a, b))
    print('ok')

