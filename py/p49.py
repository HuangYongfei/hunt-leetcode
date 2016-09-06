#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 49. Group Anagrams
# Given an array of strings, group anagrams together.


# 总结：
# 1. 排序
# 2. 利用字典

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in res:
                res[sorted_s].append(s)
            else:
                res[sorted_s] = [s]

        return [res[x] for x in res]



import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print 'ok'

