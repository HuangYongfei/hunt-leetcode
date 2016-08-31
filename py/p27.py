#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 总结：
# 1. 思路一： 两个指针i, j。从头开始找val，找到之后交换到队尾（i, j值互换）
# 2. 思路二： 由于只需要队头的值，将!=val的数按在数组中出现顺序排在队头

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, j = 0, len(nums)
        while i < j:
            if nums[i] != val:
                i += 1
            else:
                j -= 1
                nums[i], nums[j] = nums[j], nums[i]

        # print nums
        return i

    def removeElementOpt(self, nums, val):
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i;



import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().removeElement([3,2,2,3], 3)
    print Solution().removeElement([1], 1)
    # print Solution().removeElementOpt([1], 1)
    print Solution().removeElement([3], 3)
    print Solution().removeElement([2], 3)
    print Solution().removeElement([], 3)
    print 'ok'

