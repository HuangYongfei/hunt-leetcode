#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 46. Permutations
# Given a collection of distinct numbers, return all possible permutations.

# 总结：(https://discuss.leetcode.com/topic/46162/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partioning)
# 相关问题：p39&p40, p46&p47, p78&p90, p131

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        res = []
        self.backtrack(nums, path, res)
        return res

    def backtrack(self, nums, path, res):
        if len(path) == len(nums):
            # 使用切片复制数组，否则只是path的引用，会随path的改变而改变
            res.append(path[:])

        for i in range(len(nums)):
            # element already exists, skip
            if nums[i] in path:
                continue

            path.append(nums[i])
            self.backtrack(nums, path, res)
            path.pop()




import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().permute([1,2,3])
    print 'ok'

