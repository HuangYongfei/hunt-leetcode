#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 78. Subsets
# Given a set of distinct integers, nums, return all possible subsets.

# 总结：
#
# 相关问题：p39&p40, p46&p47, p78&p90, p131, p77

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        res = []
        n = len(nums)
        nums = sorted(nums)
        # self.backtrack(nums, 0, n, path, res)
        self.backtrack2(nums, 0, n, path, res)
        return res

    def backtrack(self, nums, start, n, path, res):
        # no need to if
        # if len(path) <= n:
            # res.append(path[:])
        if not path in res:
            res.append(path[:])

        for i in range(start, n):
            path.append(nums[i])
            self.backtrack(nums, i+1, n, path, res)
            path.pop()

    def backtrack2(self, nums, start, n, path, res):
        # no need to if
        # if len(path) <= n:
            # res.append(path[:])

        res.append(path[:])

        for i in range(start, n):
            #  avoid duplicates
            if i > start and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.backtrack(nums, i+1, n, path, res)
            path.pop()



import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().subsetsWithDup([1, 2, 3])
    print Solution().subsetsWithDup([1, 2, 2])
    print 'ok'

