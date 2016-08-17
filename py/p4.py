#!/usr/bin/env python
# -*- coding: utf8 -*-

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums = sorted(nums)
        n = len(nums)
        if n % 2 == 0:
            return (nums[n // 2 - 1] + nums[n // 2]) / 2.0
        return nums[n // 2] / 1.0



if __name__ == '__main__':
    print 'ok'
    print Solution().findMedianSortedArrays([1,3], [2])
    print Solution().findMedianSortedArrays([1,2], [3,4])
    print Solution().findMedianSortedArrays([1,3], [7,8,9])
    print Solution().findMedianSortedArrays([1,2,3], [7,8,9])
