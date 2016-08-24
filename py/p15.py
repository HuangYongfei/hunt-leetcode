#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 总结：
# 1. 首先排序，然后选择第一个数num（三个数中最小的）
# 2. 然后，在该数右侧数（大于num）中选择另外两个数
# 3. 另外两个数选择方式分别从两侧开始取（left 和 right）
# 4. 如果太大，right减小，如果太小，left增大（优化点1）
# 5. 如果新取的数和上一次一样，直接继续取下一个数（优化点2）

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # https://discuss.leetcode.com/topic/54656/python-two-pointer-with-explanation-intuitive-o-n-2
        n = len(nums)
        if n <= 2:
            return []
        nums, res = sorted(nums), []
        for i in range(n - 2):
            # if ith element is the same as i-1th element (say, -1). because -1 has been processed and no duplcate
            # allowed. So we just continue (skip this element.)
            if nums[i] == nums[i - 1] and i != 0:
                continue
            num = nums[i]
            left, right = i + 1, n - 1
            while left < right:
                total = num + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip all duplicate element.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total > 0:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().threeSum([-1, 0, 1, 2, -1, -4])
    print Solution().threeSum([1,-1,-1,0])
    print 'ok'

