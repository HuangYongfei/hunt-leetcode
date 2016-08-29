#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        first = dummy.next
        if not first or not first.next:
            return dummy.next
        second = first.next
        dummy.next = second
        temp3 = None
        while first and second:
            temp1 = None
            temp2 = None
            if second and second.next:
                temp1 = second.next
            if second.next and second.next.next:
                temp2 = second.next.next
            second.next = first
            first.next = temp1
            if temp3:
                temp3.next = second
            temp3 = first
            print('first.val %s, second.val %s' % (first.val, second.val))
            first = temp1
            second = temp2
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
    disp_list(Solution().swapPairs(gen_list([1, 2, 3, 4])))
    disp_list(Solution().swapPairs(gen_list([1, 2])))
    disp_list(Solution().swapPairs(gen_list([1])))
    disp_list(Solution().swapPairs(gen_list([])))
    disp_list(Solution().swapPairs(gen_list([1, 2, 3, 4, 5])))
    pass