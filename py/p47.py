#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 47. Permutations II
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# 总结：(https://discuss.leetcode.com/topic/46162/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partioning)
# 相关问题：p39&p40, p46&p47, p78&p90, p131

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # https://discuss.leetcode.com/topic/56346/my-python-solution-shorter-and-simpler-logic-than-top-rated
        # skipping duplicates, that's why i sorted first
        nums = sorted(nums)
        path = []
        res = []
        self.backtrack(nums, path, res, len(nums))
        return res

    def backtrack(self, nums, path, res, size):
        if len(path) == size:
            # 使用切片复制数组，否则只是path的引用，会随path的改变而改变
            res.append(path[:])

        for i in range(len(nums)):
            # element already exists, skip
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            path.append(nums[i])
            self.backtrack(nums[:i]+nums[i+1:], path, res, size)
            path.pop()




import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().permuteUnique([1,2,3])
    print Solution().permuteUnique([1,1,2])
    print 'ok'

