#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 75. Sort Colors
# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# 总结：
#

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero, second = 0, n - 1
        i = 0
        while i <= second:
            while i < second and nums[i] == 2:
                nums[i], nums[second] = nums[second], nums[i]
                second -= 1
            while i > zero and nums[i] == 0 :
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
            i += 1



import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print 'ok'

