#!/usr/bin/env python
# -*- coding: utf8 -*-

class Solution(object):
    # 方法1: 合并排序
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

    # 方法2：找出第 k 小的值
    # http://blog.csdn.net/yutianzuijin/article/details/11499917/

    def findMedianSortedArrays2(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if (m + n) % 2 == 1:
            return self.findKth(nums1, nums2, (m + n) // 2 + 1) / 1.0
        else:
            return (self.findKth(nums1, nums2, (m + n) // 2) + \
                    self.findKth(nums1, nums2, (m + n) // 2 + 1)) / 2.0


    @staticmethod
    def findKth(nums1, nums2, k):
        # always assume that m is equal or smaller than n
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return Solution.findKth(nums2, nums1, k)
        # 如果A或者B为空，则直接返回B[k-1]或者A[k-1]；
        if m == 0:
            return nums2[k-1]
        # 如果k为1，我们只需要返回A[0]和B[0]中的较小值；
        if k == 1:
            return min(nums1[0], nums2[0])

        # divide k into two parts
        pa = min(k // 2, m)
        pb = k - pa
        if nums1[pa-1] < nums2[pb-1]:
            # 舍弃 pa - 1个数，同时找 kth 小变为 kth-pa
            return Solution.findKth(nums1[pa:], nums2, k - pa)
        elif nums1[pa-1] > nums2[pb-1]:
            return Solution.findKth(nums1, nums2[pb:], k - pb)
        else:
            return nums1[pa-1]



# 方法2(http://blog.csdn.net/yutianzuijin/article/details/11499917/)
# 摘要：
# 该方法的核心是将原问题转变成一个寻找第k小数的问题（假设两个原序列升序排列），
# 这样中位数实际上是第(m+n)/2小的数。所以只要解决了第k小数的问题，原问题也得以解决。
# 首先假设数组A和B的元素个数都大于k/2，我们比较A[k/2-1]和B[k/2-1]两个元素，
# 这两个元素分别表示A的第k/2小的元素和B的第k/2小的元素。这两个元素比较共有三种情况：>、<和=。
# 如果A[k/2-1]<B[k/2-1]，这表示A[0]到A[k/2-1]的元素都在A和B合并之后的前k小的元素中。
# 换句话说，A[k/2-1]不可能大于两数组合并之后的第k小值，所以我们可以将其抛弃。
# 证明也很简单，可以采用反证法
# 通过上面的分析，我们即可以采用递归的方式实现寻找第k小的数。此外我们还需要考虑几个边界条件：
# 1. 如果A或者B为空，则直接返回B[k-1]或者A[k-1]；
# 2. 如果k为1，我们只需要返回A[0]和B[0]中的较小值；
# 3. 如果A[k/2-1]=B[k/2-1]，返回其中一个；

# 总结:
# 1. 问题转换：中位数变为找出第 k 小的数
# 2. 问题简化：a. 始终让 nums1 长度小于 nums2 长度
#            b. 分析问题时，先不考虑奇偶，反正无非是找第 k 小的一个数 和 找第 k,k+1小的连个数
# 3. 找第 k 小的数: a. 不断剔除不符合条件的数，范围不断缩小，同时 k 也在不断变化
#                 b. 递归的终止条件


if __name__ == '__main__':
    print 'ok'
    print Solution().findMedianSortedArrays([1,3], [2])
    print Solution().findMedianSortedArrays([1,2], [3,4])
    print Solution().findMedianSortedArrays([1,3], [7,8,9])
    print Solution().findMedianSortedArrays([1,2,3], [7,8,9])
    print Solution().findMedianSortedArrays([2], [])

    print Solution().findMedianSortedArrays2([1,3], [2])
    print Solution().findMedianSortedArrays2([1,2], [3,4])
    print Solution().findMedianSortedArrays2([1,3], [7,8,9])
    print Solution().findMedianSortedArrays2([1,2,3], [7,8,9])
    print Solution().findMedianSortedArrays2([2], [])
    print Solution().findMedianSortedArrays2([3,4], [])
