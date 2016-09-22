#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 80. Remove Duplicates from Sorted Array II
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# It doesn't matter what you leave beyond the new length.

# 总结：
# relates to: p26
# 参考：
# 1. https://discuss.leetcode.com/topic/17180/3-6-easy-lines-c-java-python-ruby
# 2. https://discuss.leetcode.com/topic/59005/1ms-java-solution

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        if n <= 1:
            return n
        count = 1
        dup_times = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count += 1
                dup_times = 1
            else:
                dup_times += 1
                if dup_times <= 2:
                    nums[count] = nums[i]
                    count += 1
        return count

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().removeDuplicates([1,1,2])
    print Solution().removeDuplicates([])
    print Solution().removeDuplicates([1,1,1,2,2,3])

    print 'ok'

