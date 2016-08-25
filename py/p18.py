#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 总结：
# 参考: p15的思想，这里nSum是用递归实现p15中的思想


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

    # https://discuss.leetcode.com/topic/54510/java-solution-16ms-beats-82-37-with-explanation
    def fourSumOpt(self, nums, target):
        n = len(nums)
        if n < 4:
            return []
        nums = sorted(nums)
        res = []
        l, h = 0, n - 1
        while l < h and nums[l] + 3 * nums[h] < target:
            l += 1
        while l < h and nums[h] + 3 * nums[l] > target:
            h -= 1

        for i in range(l, h - 2):
            if nums[i] == nums[i - 1] and i != 0:
                continue

            h2 = h
            while h2 >= i + 3:
                if h2 != h and nums[h2] == nums[h2 + 1]:
                    h2 -= 1
                    continue
                left, right = i + 1, h2 - 1
                while left < right:
                    total = nums[i] + nums[left] + nums[right] + nums[h2]
                    if total == target:
                        res.append([nums[i], nums[left], nums[right], nums[h2]])
                        left += 1
                        right -= 1
                        # skip all duplicate element.
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total > target:
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                h2 -= 1
        return res



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
    print Solution().fourSum([-1,2,2,-5,0,-1,4], 3)
    print Solution().fourSum([0, 0, 0, 0], 0)

    print Solution().fourSumOpt([1, 0, -1, 0, -2, 2], 0)
    print Solution().fourSumOpt([5,5,3,5,1,-5,1,-2], 4)
    print Solution().fourSumOpt([-1,2,2,-5,0,-1,4], 3) # [[-5,2,2,4],[-1,0,2,2]]
    print Solution().fourSumOpt([0, 0, 0, 0], 0)
    print 'ok'

