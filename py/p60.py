#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 60. Permutation Sequence
# The set [1,2,3,…,n] contains a total of n! unique permutations.
# Given n and k, return the kth permutation sequence.

# 总结：https://discuss.leetcode.com/topic/17348/explain-like-i-m-five-java-solution-in-o-n/2
# 1. 构建数组nums
# 2. 第1个数在nums中的索引index为 (k-1) / (n-1)!
# 3. nums输出移除index的数后，k = k - index*(n-1)!
# 4. 第二个数在nums中的索引为: (k-1) / (n-2)!
# 4. 以此类推：第i个数: (k-1) / (n-i)!

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        nums = [str(_) for _ in range(1,n+1)]
        k -= 1
        ans = ""
        # index_of_i = k / (n-i)!
        for i in range(n)[::-1]:
            ans += nums.pop(k / math.factorial(i))
            k %= math.factorial(i)
        return ans


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().getPermutation(3, 1)
    print Solution().getPermutation(1, 1)
    print 'ok'

