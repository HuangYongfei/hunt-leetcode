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

        # 归并的思想：分治法。从中间分成两部分，然后再合并
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

    # https://discuss.leetcode.com/topic/39467/python-quick-sort-solution-easy-to-understand-beats-95-51
    def sortList2(self, head):
        new_head = ListNode(None)
        new_head.next = head
        self.quicksort(new_head, None)
        return new_head.next

    @staticmethod
    def quicksort(start, end):
        if start.next != end:
            prev, post = Solution.partition(start, end)
            Solution.quicksort(start, prev)
            Solution.quicksort(post, end)

    @staticmethod
    def partition(start, end):
        #  We just pick the first element as pivot. And if we encounter a node with the same value as pivot, we move the pivotPost one step forward. When partition function returns, the pivot becomes the end node for the former half while the pivotPost becomes the start node for the latter half. In this way, we don't have to sort nodes between two pivots in the next round.
        node = start.next.next
        # 取第一个节点作为pivot
        pivot = start.next
        pivot.next = end
        pivotPost = pivot
        while node != end:
            temp = node.next
            if node.val > pivot.val:
                # 在post头部后插入大于当前节点的节点
                node.next = pivotPost.next
                pivotPost.next = node
            elif node.val < pivot.val:
                # 在start头部后插入下雨当前节点的节点
                node.next = start.next
                start.next = node
            else:
                # 相等时，同样在post头部后插入当前节点，并移动post
                node.next = pivotPost.next
                pivotPost.next = node
                pivotPost = pivotPost.next
            node = temp
        return [pivot, pivotPost]


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

