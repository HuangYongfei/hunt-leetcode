#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        first = dummy.next
        second = dummy.next
        while second:
            if second.val != first.val:
                first.next = second
                first = first.next
            second = second.next

        first.next = None
        return dummy.next

    def deleteDuplicates2(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


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
    disp_list(Solution().deleteDuplicates(gen_list([1])))
    disp_list(Solution().deleteDuplicates(gen_list([1, 1])))
    disp_list(Solution().deleteDuplicates(gen_list([1, 2, 3, 4, 5])))
    disp_list(Solution().deleteDuplicates(gen_list([1, 1, 2])))
    disp_list(Solution().deleteDuplicates(gen_list([1, 2, 2])))
    disp_list(Solution().deleteDuplicates(gen_list([1, 2, 2, 2, 3, 4, 4, 5, 5])))
    disp_list(Solution().deleteDuplicates(gen_list([])))
    disp_list(Solution().deleteDuplicates(gen_list([0,0,0,0,0])))


    disp_list(Solution().deleteDuplicates2(gen_list([1])))
    disp_list(Solution().deleteDuplicates2(gen_list([1, 1])))
    disp_list(Solution().deleteDuplicates2(gen_list([1, 2, 3, 4, 5])))
    disp_list(Solution().deleteDuplicates2(gen_list([1, 1, 2])))
    disp_list(Solution().deleteDuplicates2(gen_list([1, 2, 2])))
    disp_list(Solution().deleteDuplicates2(gen_list([1, 2, 2, 2, 3, 4, 4, 5, 5])))
    disp_list(Solution().deleteDuplicates2(gen_list([])))
    disp_list(Solution().deleteDuplicates2(gen_list([0,0,0,0,0])))

    print('ok')

