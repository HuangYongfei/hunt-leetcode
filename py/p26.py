#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 26. Remove Duplicates from Sorted Array
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# It doesn't matter what you leave beyond the new length.
# 总结:
# # relates to: p80
# 1. 相邻的两个数字不相等，计数加一
# 2. 同时在对应位置的数字替换为新的值（有点类似插入排序的味道）

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        count = 1
        index = 1
        end = len(nums)
        for x in range(1, end):
            if nums[x - index] != nums[x + 1 - index]:
                count += 1
            else:
                index += 1
                nums.remove(nums[x + 1 - index])
        return count

    def removeDuplicatesOpt(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        count = 1
        for x in range(1, len(nums)):
            if nums[x] != nums[x-1]:
                nums[count] = nums[x]
                count += 1
        return count

    def removeDuplicatesJustLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        count = 1
        for x in range(1, len(nums)):
            if nums[x] != nums[x-1]:
                count += 1
        return count


import unittest
class TestSolution(unittest.TestCase):
    def test_removeDuplicates(self):
        self.assertEqual(Solution().removeDuplicates([]), 0)
        self.assertEqual(Solution().removeDuplicates([1]), 1)
        self.assertEqual(Solution().removeDuplicates([1, 2, 2, 3]), 3)
        self.assertEqual(Solution().removeDuplicates([1, 2, 3]), 3)
        self.assertEqual(Solution().removeDuplicates([1, 1, 1]), 1)
        self.assertEqual(Solution().removeDuplicates([1, 2, 2, 3, 4, 4, 5]), 5)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print 'ok'