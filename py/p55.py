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
# 5. greedy: 依次找出每个位置下，可达的最大位置

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
        # for next_pos in range(pos+1, furtest_jump+1):
        for next_pos in range(furtest_jump, pos, -1):
            if self.backtrack(nums, next_pos, size):
                return True

        return False


    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # unknown(0), good(1), bad(2)
        memo = [0] * len(nums)
        memo[len(nums) - 1] = 1
        return self.dp_top_down(nums, 0, len(nums), memo)

    def dp_top_down(self, nums, pos, size, memo):
        # not unknown
        if memo[pos]:
            return True if memo[pos] == 1 else False

        furtest_jump = min(pos+nums[pos], size - 1)
        for next_pos in range(pos+1, furtest_jump+1):
            if self.dp_top_down(nums, next_pos, size, memo):
                # good
                memo[pos] = 1
                return True

        # bad
        memo[pos] = 2
        return False


    def canJump3(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.dp_bottom_up(nums)

    def dp_bottom_up(self, nums):
        size = len(nums)
        memo = [0] * size
        memo[size-1] = 1

        for i in range(size-2, -1, -1):
            furtest_jump = min(i+nums[i], size-1)
            for j in range(i+1, furtest_jump+1):
                if memo[j] == 1:
                    memo[i] = 1
                    break

        return memo[0] == 1

    def canJump4(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.greedy(nums)

    def greedy(self, nums):
        size = len(nums)
        left_most_good = size - 1

        for i in range(size-1, -1, -1):
            if i + nums[i] >= left_most_good:
                left_most_good = i

        return left_most_good == 0

    def canJump5(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        furtest = 0
        size = len(nums)
        for i in range(size):
            # 在 i 这个位置，其前面最远只能到 furtest < i
            # 说明在 i 之前到达不了 i
            if i > furtest:
                return False
            furtest = max(i+nums[i], furtest)
            # if furtest >= size - 1:
            #     return True
        return True

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print '==backtracking=='
    print Solution().canJump([2,3,1,1,4])
    print Solution().canJump([3,2,1,0,4])

    print '==dp top down=='
    print Solution().canJump2([2,3,1,1,4])
    print Solution().canJump2([3,2,1,0,4])


    print '==dp bottom up=='
    print Solution().canJump3([2,3,1,1,4])
    print Solution().canJump3([3,2,1,0,4])

    print '==greedy=='
    print Solution().canJump4([2,3,1,1,4])
    print Solution().canJump4([3,2,1,0,4])


    print '==furtest=='
    print Solution().canJump5([2,3,1,1,4])
    print Solution().canJump5([3,2,1,0,4])

    print 'ok'

