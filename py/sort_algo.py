#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 总结：
#

def quicksort(arr):
    quicksort_helper(arr, 0, len(arr)-1)
    print arr

def quicksort_helper(arr, left, right):
    # if left >= right:
    #   return
    # or:
    if left < right:
        i, j = left, right
        pivot = arr[left]
        while i < j:
            # 从右到左找出第一个小于pivot的数，位置为j，并将其替换到i的位置
            while i < j and arr[j] >= pivot:
                j -= 1
            if i < j:
                arr[i] = arr[j]
                i += 1

            # 从左到右找出第一个大于pivot的数，位置为i，并将其替换到j的位置
            while i < j and arr[i] <= pivot:
                i += 1
            if i < j:
                arr[j] = arr[i]
                j -= 1
        # 更新pivot的位置到中间（中间指：左边的值都比pivot小，右边的值都比pivot大）
        arr[i] = pivot
        quicksort_helper(arr, left, i - 1)
        quicksort_helper(arr, i + 1, right)

def quicksort2(arr, left, right):
    if left >= right:
        return
    # k 表示小于pivot的下标
    k = left
    for i in range(left+1, right+1):
        # pivot：左边的元素（可以选择右边的元素）
        # 小于pivot的交换到前面
        if arr[i] < arr[left]:
            k += 1
            arr[k], arr[i] = arr[i], arr[k]
    # 将pivot交换到中间
    arr[k], arr[left] = arr[left], arr[k]
    quicksort2(arr, left, k-1)
    quicksort2(arr, k+1, right)


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    quicksort([1,3,4,2,5])
    quicksort([1,3,4,2,5,7,10,9,8])
    quicksort([])
    quicksort([1])
    arr = [1,3,4,2,5]
    quicksort2(arr, 0, len(arr)-1)
    print arr
    arr = [1,3,4,2,5,7,10,9,8]
    quicksort2(arr, 0, len(arr)-1)
    print arr
    arr = [1]
    quicksort2(arr, 0, len(arr)-1)
    print arr
    arr = []
    quicksort2(arr, 0, len(arr)-1)
    print arr
    print 'ok'

