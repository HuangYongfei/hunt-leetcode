#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# 82. Remove Duplicates from Sorted List II
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.



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

        dummy = ListNode("dummy")
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            if current.next.val == current.next.next.val:
                while current.next.next and current.next.val == current.next.next.val:
                    current.next = current.next.next
                if current.next:
                    current.next = current.next.next
            else:
                current = current.next

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
    disp_list(Solution().deleteDuplicates(gen_list([1, 2, 3, 3, 4, 4, 5])))
    disp_list(Solution().deleteDuplicates(gen_list([1, 1, 1, 2, 3])))

    # disp_list(Solution().deleteDuplicates(gen_list([1])))
    # disp_list(Solution().deleteDuplicates(gen_list([1, 1])))
    # disp_list(Solution().deleteDuplicates(gen_list([1, 2, 3, 4, 5])))
    # disp_list(Solution().deleteDuplicates(gen_list([1, 1, 2])))
    # disp_list(Solution().deleteDuplicates(gen_list([1, 2, 2])))
    # disp_list(Solution().deleteDuplicates(gen_list([1, 2, 2, 2, 3, 4, 4, 5, 5])))
    # disp_list(Solution().deleteDuplicates(gen_list([])))
    # disp_list(Solution().deleteDuplicates(gen_list([0,0,0,0,0])))


    print('ok')

