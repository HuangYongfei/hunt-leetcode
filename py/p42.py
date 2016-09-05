#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 42. Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# 总结：
# 1. 方法一：面积相减
# 2. 方法二：直接计算

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0

        # 1. 求出最大值和位置，并计算所有柱行的面积和
        max_num = height[0]
        pos = 0
        sum_height = 0
        for i in range(len(height)):
            sum_height += height[i]
            if height[i] > max_num:
                max_num, pos = height[i], i

        # 2. 根据最大值分成左右两部分，进行面积计算（便于计算，将右侧的图形反转）
        h1 = height[:pos+1]
        # h2 = height[pos:][::-1]
        # 使用负索引
        h2 = height[-1:pos-len(height)-1:-1]
        # print max_num, pos, h1, h2
        # 3. 求左边和右边的面积
        sum_h1 = 0
        sum_h2 = 0
        if len(h1) > 2:
            low_pos, low_val = 0, h1[0]
            # 计算左边带雨水情况下的面积
            for i in range(1, len(h1)):
                if h1[i] >= low_val:
                    sum_h1 += low_val * (i - low_pos)
                    low_pos, low_val = i, h1[i]
            # 算上最后一个柱行面积
            sum_h1 += h1[-1]
        else:
            for val in h1:
                sum_h1 += val

        if len(h2) > 2:
            low_pos, low_val = 0, h2[0]
            # 计算左边带雨水情况下的面积
            for i in range(1, len(h2)):
                if h2[i] >= low_val:
                    sum_h2 += low_val * (i - low_pos)
                    low_pos, low_val = i, h2[i]
            # 算上最后一个柱行面积
            sum_h2 += h2[-1]
        else:
            for val in h2:
                sum_h2 += val

        # 左边和右边重复计算了两次max_num
        return sum_h1 + sum_h2 - max_num - sum_height

    def trap2(self, height):
        left, right = 0, len(height) - 1
        res = 0
        max_left, max_right = 0, 0
        while left <= right:
            # 使用两者的局部最大值作为全局最大值，可以确保操作的方向正确性
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    res += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    res += max_right - height[right]
                right -= 1

        return res


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])  # 6
    print Solution().trap([2,0,2])  # 2
    print Solution().trap2([0,1,0,2,1,0,1,3,2,1,2,1])  # 6
    print Solution().trap2([2,0,2])  # 2
    print 'ok'

