#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import

# 81. Search in Rotated Sorted Array II

# 总结：relates to p33
#


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        low, high = 0, n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True
            if nums[low] < nums[mid]:  # left half is sorted
                if nums[low] <= target and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[low] > nums[mid]:  # right half is sorted
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                low += 1

        return False



import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print('ok')

