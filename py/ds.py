#!/usr/bin/env python
# -*- coding: utf8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class List(object):
    root = None
    size = 0
    def __init__(self, new_root):
        self.root = new_root

    def __init__(self):
        self.root = None
        size = 0

    def insert(self, data):
        new_node = ListNode(data)
        if self.root is None:
            self.root = new_node
            return
        temp_node = self.root
        while temp_node.next:
            temp_node = temp_node.next
        temp_node.next = new_node
        self.size += 1

    def disp(self):
        l = self.root
        while (l):
            print l.val
            l = l.next


if __name__ == '__main__':
    print 'ok'
    a = List()
    for x in xrange(0, 3):
        a.insert(x)
    a.disp()
