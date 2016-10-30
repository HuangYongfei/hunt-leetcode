#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# 147. Insertion Sort List
# Sort a linked list using insertion sort.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        dummy = ListNode(None)
        # dummy.next = head
        prev = dummy
        curr = head
        while curr:
            temp = curr.next
            # 从头开始(每次循环开始prev都处于dummy)找到下一个合适的位置(prev 和 prev.next之间)
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            # insert between prev and prev.next
            curr.next = prev.next
            prev.next = curr
            curr = temp
            # 保证每次循环开始prev都处于dummy
            prev = dummy

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
    print(disp_list(Solution().insertionSortList(gen_list([1]))))
    print('ok')

