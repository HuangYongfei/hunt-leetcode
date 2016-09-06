#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 53. Maximum Subarray
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# 总结：
# 1. 累计子数组的和sub_sum
# 2. 如果 sub_sum + nums[i] <= nums[i],
#      说明前面累计的子数组加上nums[i]的数组和较小，nums[i]可能作为一个新的子数组的开始
#      反之，将nums[i]的值计入到sub_sum
# 3. max_sum = max(sub_sum, max_sum)


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # no necessry an array (containing at least one number)
        # n = len(nums)
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return nums[0]

        # (containing at least one number)
        sub_sum, max_sum = nums[0], nums[0]
        for num in nums[1:]:
            # if sub_sum + num > num:
            #     sub_sum += num
            # else:
            #     sub_sum = num

            sub_sum = max(sub_sum + num, num)
            max_sum = max(sub_sum, max_sum)

        return max_sum

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print Solution().maxSubArray([-1,0,-2])
    print 'ok'

