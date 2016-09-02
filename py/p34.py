#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        low, high = -1, -1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                # 确定中间值
                low, high = mid, mid
                # 分别查找左右边界
                while left <= low:
                    # 找到最左侧的target
                    if nums[left] == target:
                        low = left
                        break
                    temp = (low - left) // 2 + left
                    # print left, low, temp
                    if nums[temp] < target:
                        left = temp + 1
                    elif nums[temp] == target:
                        low = temp
                while high <= right:
                    # 找到最右侧的target
                    if nums[right] == target:
                        high = right
                        break
                    temp = (right - high) // 2 + high
                    # print high, right, temp
                    if nums[temp] > target:
                        right = temp - 1
                    elif nums[temp] == target:
                        high = temp
                        # 防止出现 temp = right - 1, nums[temp] == target, nums[right] != target
                        right = right - 1
                return [low, high]
        return [low, high]

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
    print Solution().searchRange([8], 8)
    print Solution().searchRange([8,8], 8)
    print Solution().searchRange([0], 8)
    print Solution().searchRange([1,2,3,8], 8)
    print Solution().searchRange([1,2,3,3,3,3,4,5,9], 3)

    print 'ok'

