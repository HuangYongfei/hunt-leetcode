#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 总结:
# 1. 从最左和最右开始计算
# 2. 水量由最低的高度决定
# 3. 获取当前最大水量，然后将最低的板右移(左边低)或左移(右边低)

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        l = 0
        r = len(height) - 1
        while l < r:
            if height[l] <= height[r]:
                water = max(water, (r - l) * height[l])
                l += 1
            else:
                water = max(water, (r - l) * height[r])
                r -= 1
        return water

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print 'ok'



