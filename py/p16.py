#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 总结：
# 参考p15

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return target
        res = nums[0] + nums[1] + nums[2]
        closest = 0
        if res >= target:
            closest = res - target
        else:
            closest = target - res

        nums = sorted(nums)
        for i in range(n - 2):
            if nums[i] == nums[i - 1] and i != 0:
                continue
            num, left, right = nums[i], i + 1, n - 1
            while left < right:
                total = num + nums[left] + nums[right]
                if total == target:
                    return total
                elif total > target:
                    closest, res = (closest, res) if total - target > closest else (total - target, total)
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:
                    closest, res = (closest, res) if target - total > closest else (target - total, total)
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().threeSumClosest([-1,2,1,-4], 1)
    print 'ok'

