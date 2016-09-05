#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 39. Combination Sum
# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
# The same repeated number may be chosen from C unlimited number of times.

# 总结：（https://discuss.leetcode.com/topic/54641/4ms-98-java-dfs-neat-code）
# 1. dfs
# 2. 设置 boundary 防止重复


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        # candidates.sort()
        res = []
        path = []
        self.dfs_com(candidates, 0, target, path, res)
        return res

    def dfs_com(self, candidates, boundary, target, path, res):
        if target == 0:
            # 使用切片复制数组，否则只是path的引用，会随path的改变而改变
            res.append(path[:])
            return
        if target < 0:
            return

        for val in candidates:
            if val >= boundary and (val == target or target - val >= boundary):
                path.append(val)
                self.dfs_com(candidates, val, target - val, path, res)
                path.pop()



import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().combinationSum([2, 3, 6, 7], 7)
    print 'ok'

