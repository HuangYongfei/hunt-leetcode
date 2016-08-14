#!/usr/bin/env python
# -*- coding: utf8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry_bit = 0
        prev = head = None
        while l1 or l2 or carry_bit:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry_bit
            val, carry_bit = sum % 10, sum / 10
            node = ListNode(val)
            if not head:
                prev = head = node
            else:
                prev.next = node
                prev = prev.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
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
        print l.val
        l = l.next

if __name__ == '__main__':
    print 'ok'
    a = gen_list([2,4,3])
    b = gen_list([5,6,4])
    disp_list(a)
    disp_list(b)
    c = Solution().addTwoNumbers(a, b)
    disp_list(c)
