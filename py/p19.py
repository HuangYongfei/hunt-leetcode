#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or n <= 0:
            return head

        pprev = prev = head
        k = 0
        while prev.next and k < n:
            pprev = prev
            prev = prev.next
            k += 1

        # print('k: %s, n: %s, prev: %s' % (k, n, prev.val))
        if k < n - 1:
            return head

        nth_node = head
        while prev.next:
            prev = prev.next
            nth_node = nth_node.next

        # print('nth %s' % nth_node.val)

        # k == 0, 说明长度为1
        if nth_node == head and k == 0:
            return []
        # 删除头部
        if nth_node == head and k == n - 1:
            head = head.next

        nth_node.next = nth_node.next.next
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
    disp_list(Solution().removeNthFromEnd(gen_list([1, 2, 3, 4, 5]), 2))
    disp_list(Solution().removeNthFromEnd(gen_list([1, 2, 3, 4, 5]), 1))
    disp_list(Solution().removeNthFromEnd(gen_list([1, 2, 3, 4, 5]), 5))
    disp_list(Solution().removeNthFromEnd(gen_list([1, 2, 3, 4, 5]), 8))
    disp_list(Solution().removeNthFromEnd(gen_list([1, 2]), 1))
    disp_list(Solution().removeNthFromEnd(gen_list([1, 2]), 2))

    disp_list(Solution().removeNthFromEnd(gen_list([1]), 1))
    disp_list(Solution().removeNthFromEnd(gen_list([]), 1))

    print('ok')

