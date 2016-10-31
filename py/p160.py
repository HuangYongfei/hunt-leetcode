#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# 160. Intersection of Two Linked Lists
# Write a program to find the node at which the intersection of two singly linked lists begins.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        import gc
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        # the idea is if you switch head, the possible difference between length would be countered.
        # On the second traversal, they either hit or miss.
        # if they meet, pa or pb would be the node we are looking for,
        # if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None
        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        # clean the memory
        gc.collect()

        # only 2 ways to get out of the loop, they meet or the both hit the end=None
        return pa

    # 另一个思路就是先求出两个链表的长度，然后将长的链表先移动长度差步数
    def getIntersectionNode2(self, headA, headB):
        import gc
        lenA = lenB = 0
        p1, p2 = headA, headB
        while p1:
            lenA += 1
            p1 = p1.next

        gc.collect()
        while p2:
            lenB += 1
            p2 = p2.next
        gc.collect()

        (l1, l2) = (headA, headB) if lenA > lenB else (headB, headA)
        for _ in range(abs(lenA-lenB)):
            l1 = l1.next

        while l1:
            # when l1 is l2 or l1 = l2 = None
            if l1 is l2:
                return l1
            l1, l2 = l1.next, l2.next


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

