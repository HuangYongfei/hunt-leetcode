#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# 206. Reverse Linked List
# Reverse a singly linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        while head:
            temp = head.next
            head.next = new_head
            new_head = head
            head = temp
        return new_head

    def reverse_list_recur(head):
        return self.reverse_list_recur_helper(head, None)

    def reverse_list_recur_helper(self, head, new_head):
        if not head:
            return new_head
        temp = head.next
        head.next = new_head
        return self.reverse_list_recur_helper(temp, head)



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
    disp_list(Solution().reverseList(gen_list([1, 2, 3, 4, 5])))
    disp_list(Solution().reverseList(gen_list([1, 2])))

    disp_list(Solution().reverseList(gen_list([1])))
    disp_list(Solution().reverseList(gen_list([])))


    # disp_list(Solution().removeNthFromEndWithDummy(gen_list([1]), 8))

    print('ok')

