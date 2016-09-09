#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 66. Plus One
# Given a non-negative number represented as an array of digits, plus one to the number.
# The digits are stored such that the most significant digit is at the head of the list.

# 总结：
#

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        n = len(digits)
        digits[n-1] += 1
        for i in range(n-1, -1, -1):
            temp = digits[i] + carry
            digits[i] = temp % 10
            carry = temp / 10
        if carry:
            digits = [carry] + digits
        return digits

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().plusOne([1,2,1])
    print Solution().plusOne([9])
    print Solution().plusOne([8,8,9])
    print Solution().plusOne([8,9,9])
    print Solution().plusOne([9,9,9])
    print 'ok'

