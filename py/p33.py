#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import

# 33. Search in Rotated Sorted Array


# 总结：
# https://discuss.leetcode.com/topic/3538/concise-o-log-n-binary-search-solution


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low, high = 0, n - 1
        # find the index of the smallest value using binary search.
        # Loop will terminate since mid < high, and low or high will shrink by at least 1.
        # Proof by contradiction that mid < high: if mid==high, then low==high and loop would have been terminated.

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        # low==high is the index of the smallest value and also the number of places rotated.
        rotate = low
        low, high = 0, n - 1
        # The usual binary search and accounting for rotation
        while low <= high:
            mid = low + (high - low) // 2
            realmid = (mid + rotate) % n
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print('ok')

