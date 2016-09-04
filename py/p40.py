#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def combinationSum2(self, candidates, target):
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

    def dfs_com(self, candidates, cur, target, path, res):
        if target == 0:
            # 使用切片复制数组，否则只是path的引用，会随path的改变而改变
            res.append(path[:])
            return
        if target < 0:
            return

        for i in range(cur, len(candidates)):
            if i > cur and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            self.dfs_com(candidates, i + 1, target - candidates[i], path, res)
            path.pop()



import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    print 'ok'

