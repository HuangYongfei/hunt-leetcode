#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 41. First Missing Positive
# Given an unsorted integer array, find the first missing positive integer.
# Your algorithm should run in O(n) time and uses constant space.


# 总结：
# 1. 最多需要有n = len(nums) 个正整数
# 2. 将正确的值n>=nums[i]>0填入到数组的正确位置 nums[i] - 1
# 3. 找出第一个不正确的数值nums[nums[i]-1] != i+1

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            # 找出正确的值并填入到数组合适的位置

            while nums[i] > 0 and nums[i] <= n and \
            nums[i] != nums[nums[i] - 1]:
                # 这里有个坑，要注意交换的顺序，这么写是错误的：nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]，它等价于：
                # temp=nums[i]
                # nums[i] = nums[nums[i]-1]
                # nums[nums[i]-1] = temp  （注意这里的下标nums[i]-1已经改变了）
                # 所以应该是：
                # temp = nums[nums[i]-1]
                # nums[nums[i]-1] = nums[i]
                # nums[i] = temp   (这里的下标i不会改变)
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().firstMissingPositive([1,2,0])
    print Solution().firstMissingPositive([3,4,-1,1])
    print 'ok'

