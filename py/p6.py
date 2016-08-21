#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        # 取出每行被 2 * numRows - 2 整除后的余数
        mod_arr = []
        mod_num = 2 * numRows - 2
        for i in range(0, numRows):
            if i == 0 or i == numRows - 1:
                mod_arr.append((i,))
            else:
                mod_arr.append((i,  mod_num - i))

        # Time Limit Exceeded
        n = len(s)
        r_s = ''
        for j in range(0, numRows):
            for x in range(0, n):
                if x % mod_num in mod_arr[j]:
                    r_s += s[x]
        return r_s

    def convertOpt(self, s, numRows):
        # https://discuss.leetcode.com/topic/54012/python-solution-o-n-with-picture-to-understand
        if numRows == 1:
            return s

        n = len(s)
        mod_num = 2 * numRows - 2
        wordlist=[""] * numRows
        # 根据下标规律，将修正后的下标保存到对应的charclass中
        # 然后根据下标获得新的wordlist
        charclass=[0] * n
        for i in range(n):
            charclass[i] = i % mod_num
            # 判断是否从下到上
            if charclass[i] > numRows - 1:
                charclass[i]= mod_num - charclass[i]
        for i in range(n):
            wordlist[charclass[i]] += (s[i])
        return "".join(wordlist)




import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    # print Solution().convert('PAYPALISHIRING', 1)
    print Solution().convert('PAYPALISHIRING', 3)
    # print Solution().convertOpt('PAYPALISHIRING', 1)
    print Solution().convertOpt('PAYPALISHIRING', 3)
    print 'ok'

