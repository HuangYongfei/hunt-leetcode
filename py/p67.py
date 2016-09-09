#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 67. Add Binary
# Given two binary strings, return their sum (also a binary string).

# 总结：
#

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        res = []
        len_a = len(a)
        len_b = len(b)
        i, j = len_a-1, len_b - 1
        while i >= 0 and j>= 0:
            sum = int(a[i]) + int(b[j]) + carry
            val, carry = sum % 2, sum / 2
            res.append(str(val))
            i -= 1
            j -= 1

        while i >= 0:
            sum = int(a[i]) + carry
            val, carry = sum % 2, sum / 2
            res.append(str(val))
            i -= 1

        while j >= 0:
            sum = int(b[j]) + carry
            val, carry = sum % 2, sum / 2
            res.append(str(val))
            j -= 1

        if carry:
            res.append(str(carry))


        return ''.join(res[::-1])



import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().addBinary([1, 1], [1])
    print Solution().addBinary([1, 1], [])
    print Solution().addBinary([1, 0], [1])
    print Solution().addBinary([0], [1])
    print Solution().addBinary([1, 0], [1, 1, 1])
    print 'ok'

