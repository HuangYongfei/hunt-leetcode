#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        nums = [
                ['a', 'b', 'c'],
                ['d', 'e', 'f'],
                ['g', 'h', 'i'],
                ['j', 'k', 'l'],
                ['m', 'n', 'o'],
                ['p', 'q', 'r', 's'],
                ['t', 'u', 'v'],
                ['w', 'x', 'y', 'z'],
            ]
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            dig = int(digits[0])
            if dig == 0 or dig == 1:
                return []
            else:
                return nums[dig - 2]


        res = ['']
        for dig in digits:
            x = int(dig)
            if x == 0 or x == 1:
                continue
            res = [i+j for i in res for j in nums[x-2]]

        # print len(res)
        return res

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().letterCombinations('23')
    print Solution().letterCombinations('')
    print Solution().letterCombinations('0')
    print Solution().letterCombinations('1')
    print Solution().letterCombinations('2')
    print Solution().letterCombinations('0123')
    print 'ok'

