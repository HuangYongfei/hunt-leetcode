#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 45. Jump Game II
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.


# 总结：relates to p55
# 1. 思路：https://discuss.leetcode.com/topic/4069/sharing-my-ac-java-solution
#    总是找出到达某个位置的最小步数

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # <i 到达的最远地方为furtest
        furtest = 0
        step = 0
        # 在i及其i所在位置可到达的最大位置
        furtest_before_i = 0
        size = len(nums)
        for i in range(0, size-1):
            # 在 i 这个位置，其前面最远只能到 furtest < i
            # 说明在 i 之前到达不了 i
            if i > furtest:
                break

            # 在i位置，到达的最远的地方
            furtest_before_i = max(furtest_before_i, nums[i] + i)
            # i 到达上一次的furtest位置时，更新furtest为furtest_before_i
            # 同时次数 +1
            if i == furtest:
                furtest = furtest_before_i
                step += 1

        return step if furtest >= size - 1 else -1


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().jump([2,3,1,1,4])
    print Solution().jump([0])
    print Solution().jump([2,1])
    print 'ok'

