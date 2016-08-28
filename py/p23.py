#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # https://discuss.leetcode.com/topic/54252/simple-python-solution
        heap = []
        for lst in lists:
            if lst:
                heapq.heappush(heap, (lst.val, lst.next))
        ret = []
        while heap:
            head, lst = heapq.heappop(heap)
            ret.append(head)
            if lst:
                heapq.heappush(heap, (lst.val, lst.next))
        return ret

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print 'ok'

