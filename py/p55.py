#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 55. Jump Game
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.



# 总结：
# 分析思路强力推荐： https://leetcode.com/articles/jump-game/
# 1. backtracking
# 2. dp(top-down)
# 3. dp(bottom-up)
# 4. greedy

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.backtrack(nums, 0, len(nums))

    def backtrack(self, nums, pos, size):
        if pos == size - 1:
            return True

        furtest_jump = min(pos+nums[pos], size-1)
        for next_pos in range(pos+1, furtest_jump+1):
            if self.backtrack(nums, next_pos, size):
                return True

        return False

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().canJump([2,3,1,1,4])
    print Solution().canJump([3,2,1,0,4])
    print 'ok'

