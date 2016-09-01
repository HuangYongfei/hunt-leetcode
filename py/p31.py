#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Find largest index i where nums[i] < nums[i + 1]
        # Find lasgest index j after i where nums[j] > nums[i]
        # Swap node nums[i] and nums[j]
        # Reverse from index i to the end.
        n = len(nums)
        i, j = n - 1, n - 1
        while i > 0:
            if nums[i] > nums[i-1]:
                while j > i - 1:
                    if nums[j] > nums[i-1]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        nums[i:] = sorted(nums[i:])
                        print nums
                        return None
                    j -= 1

            i -= 1

        nums.reverse()
        print nums
        return None


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    # print Solution().nextPermutation([1,2,3])
    print Solution().nextPermutation([1,3,2])
    # print Solution().nextPermutation([3,2,1])
    # print Solution().nextPermutation([1,1,5])
    print 'ok'

