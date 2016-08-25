#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 总结：
# 1. 首先排序，然后选择第一个数num（三个数中最小的）
# 2. 然后，在该数右侧数（大于num）中选择另外两个数
# 3. 另外两个数选择方式分别从两侧开始取（left 和 right）
# 4. 如果太大，right减小，如果太小，left增大（优化点1）
# 5. 如果新取的数和上一次一样，直接继续取下一个数（优化点2）

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        nums = sorted(nums)
        return nSum(nums, 0, 4, target)

# https://discuss.leetcode.com/topic/54009/simple-java-solution-for-4-sum-3-sum-2-sum-any-sum
def nSum(nums, start, n, target):
    res = []
    l = len(nums)
    # target is too small or too large so that there won't be solutions
    if target < nums[start] * n or target > nums[l - 1] * n:
        return res
    for i in range(start, l - n + 1):
        # avoid duplicated solutions
        if i > start and nums[i - 1] == nums[i]:
            continue
        if n == 1:
            # binary search can be used here to improve performance
            if target > nums[i]:
                continue
            if target < nums[i]:
                break
            res.append([target])
            break

        temp = []
        for j in nSum(nums, i + 1, n - 1, target - nums[i]):
            j.append(nums[i])
            res.append(j)

    # print res
    return res

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
    print Solution().fourSum([5,5,3,5,1,-5,1,-2], 4)
    print 'ok'

