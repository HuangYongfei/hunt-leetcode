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
        sum = 0
        head = None
        temp = None
        while (l1 != None and l2 != None):
            sum = (l1.val + l2.val + carry_bit) % 10
            carry_bit = (l1.val + l2.val + carry_bit) / 10
            node = ListNode(sum)
            if not head:
                head = node
                temp = head
            else:
                temp.next = node
                temp = temp.next
            l1 = l1.next
            l2 = l2.next

        while (l1 != None):
            sum = (l1.val + carry_bit) % 10
            carry_bit = (l1.val + carry_bit) / 10
            node = ListNode(sum)
            if not head:
                head = node
                temp = head
            else:
                temp.next = node
                temp = temp.next
            l1 = l1.next

        while (l2 != None):
            sum = (l2.val + carry_bit) % 10
            carry_bit = (l2.val + carry_bit) / 10
            node = ListNode(sum)
            if not head:
                head = node
                temp = head
            else:
                temp.next = node
                temp = temp.next

            l2 = l2.next

        if carry_bit:
            node = ListNode(carry_bit)
            if not head:
                head = node
                temp = head
            else:
                temp.next = node
                temp = temp.next

        return head

def gen_list(arr):
    head = None
    temp = None
    for x in arr:
        node = ListNode(x)
        if not head:
            head = node
            temp = head
        else:
            temp.next = node
            temp = temp.next
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
