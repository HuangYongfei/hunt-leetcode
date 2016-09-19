#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 77. Combinations
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# 总结：
# 相关问题：p39&p40, p46&p47, p78&p90, p131, p77


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        path = []
        res = []
        self.backtrace(n, k, 1, path, res)
        return res

    # TLE
    def backtrace(self, n, k, start, path, res):
        if len(path) == k:
            # 使用切片复制数组，否则只是path的引用，会随path的改变而改变
            res.append(path[:])
            return

        print start
        for i in range(start, n+1):
            path.append(i)
            print i, path
            self.backtrace(n, k, i+1, path, res)
            path.pop()

    # 剪枝：剩余的数不够时及时返回
    def backtrace2(self, n, k, start, path, res):
        if len(path) == k:
            # 使用切片复制数组，否则只是path的引用，会随path的改变而改变
            res.append(path[:])
            return

        for i in range(start, n+1):
            # You can stop much earlier if you notice that number of remaining elements is smaller than needed to fill combination
            if n - start + 1 < k - len(path):
                return
            path.append(i)
            self.backtrace2(n, k, i+1, path, res)
            path.pop()

    # 剪枝：同2
    def backtrace3(self, n, k, start, path, res):
        if 0 == k:
            # 使用切片复制数组，否则只是path的引用，会随path的改变而改变
            res.append(path[:])
            return

        for i in range(start, n-k+1+1):
            path.append(i)
            self.backtrace3(n, k-1, i+1, path, res)
            path.pop()

    # itertools
    def combine2(self, n, k):
        import itertools
        return [each for each in itertools.combinations(range(1, n + 1), k)]

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().combine(4, 2)
    # print Solution().combine2(4, 2)
    # print Solution().combine(20, 16)
    print 'ok'

