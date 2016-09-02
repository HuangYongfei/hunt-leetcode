#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 总结：
# 1. 原理：将每行，每列，每单元格出现的数字用字典保存起来
# 2. 实现：遍历board，如果该位置的元素在对应的行，列或单元格字典中出现过，则直接返回
#         否则，添加进字典
# 3. 优化：构建字典的时候通过构建新的key：https://discuss.leetcode.com/topic/27436/short-simple-java-using-strings
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        map_row = [{} for _ in range(9)]
        map_col = [{} for _ in range(9)]
        map_cell = [[{} for _ in range(3)] for __ in range(3)]
        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch != '.':
                    if ch in map_row[i]:
                        return False
                    else:
                        map_row[i][ch] = (i, j)
                    if ch in map_col[j]:
                        return False
                    else:
                        map_col[j][ch] = (i, j)
                    if ch in map_cell[i/3][j/3]:
                        return False
                    else:
                        map_cell[i/3][j/3][ch] = (i, j)
        return True

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print 'ok'

