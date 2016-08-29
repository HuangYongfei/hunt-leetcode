#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# 总结： 参考 p24
# 1. 先取出链表中 k 个节点
# 2. current 记录 k 个节点的前一个节点
# 3. 第 k 个节点的 第一个节点（first）的next 指向 第 k+1
# 4. k 个节点中的 最后一个节点的前一节点是 上 k 个节点的最后一个节点的next
# 5. 反转这 k 个节点

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # https://discuss.leetcode.com/topic/55969/python-solution-o-n-and-just-76ms
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        end_node = dummy
        while True:
            n = 0
            while n < k:
                end_node = end_node.next
                if not end_node:
                    return dummy.next

                n += 1

            # 第 k 个节点
            temp = end_node
            # 第 k + 1 个节点
            end_node = end_node.next
            # k 个节点中的第"一"个节点
            first = current.next
            # k 个节点中的第"二"个节点
            second = current.next.next
            # 第 k 个节点的 第一个节点（first）的next 指向 第 k+1
            first.next = end_node
            # k 个节点中的 最后一个节点的前一节点是 上 k 个节点的最后一个节点的next
            current.next = temp
            # 记住该 k 个节点的最后一个节点，作为下 k 个节点的 current
            next_current_node = first
            # 逆转 k 个节点
            for i in range(k - 1):
                temp = second.next
                second.next = first
                first = second
                second = temp

            current = end_node = next_current_node



    def swapPairs2(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = current.next.next

            current.next = second
            first.next = second.next
            second.next = first

            current = current.next.next
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