#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 61. Rotate List
# Given a list, rotate the list to the right by k places, where k is non-negative.

from __future__ import print_function

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        first = second = dummy
        list_len = 0
        while first.next:
            first = first.next
            list_len += 1

        if list_len:
            k = k % list_len
        for i in xrange(k):
            if not first.next:
                first = dummy
            first = first.next

        while first and first.next:
            first = first.next
            second = second.next

        if second and second.next and second != dummy:
            first.next = dummy.next
            dummy.next = second.next
            second.next = None

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
    disp_list(Solution().rotateRight(gen_list([1, 2, 3, 4, 5]), 0))
    disp_list(Solution().rotateRight(gen_list([1, 2, 3, 4, 5]), 1))
    disp_list(Solution().rotateRight(gen_list([1, 2, 3, 4, 5]), 2))
    disp_list(Solution().rotateRight(gen_list([1, 2, 3, 4, 5]), 3))
    disp_list(Solution().rotateRight(gen_list([1, 2, 3, 4, 5]), 4))
    disp_list(Solution().rotateRight(gen_list([1, 2, 3, 4, 5]), 5))
    disp_list(Solution().rotateRight(gen_list([1, 2, 3, 4, 5]), 6))
    disp_list(Solution().rotateRight(gen_list([1, 2, 3, 4, 5]), 7))
    # disp_list(Solution().rotateRight(gen_list([1, 2]), 1))
    # disp_list(Solution().rotateRight(gen_list([1, 2]), 2))

    # disp_list(Solution().rotateRight(gen_list([1]), 1))
    # disp_list(Solution().rotateRight(gen_list([]), 1))


    # disp_list(Solution().removeNthFromEndWithDummy(gen_list([1]), 8))

    print('ok')

