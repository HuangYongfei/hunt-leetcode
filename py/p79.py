#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 79. Word Search
# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# 总结：
# dfs
# 参考：
# 1. https://discuss.leetcode.com/topic/12391/python-simple-dfs-solution
# 2. https://discuss.leetcode.com/topic/22788/python-dfs-solution-with-comments

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True

        return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word):
        if board[i][j] == word[0]:
            # all characters are checked
            if not word[1:]:
                return True
            # tmp = board[i][j]  # first character is found, check the remaining part
            board[i][j] = "#"  # avoid visit agian
            # check all adjacent cells
            if i > 0 and self.dfs(board, i-1, j, word[1:]):
                return True
            if i < len(board) - 1 and self.dfs(board, i+1, j, word[1:]):
                return True
            if j > 0 and self.dfs(board, i, j-1, word[1:]):
                return True
            if j < len(board[0]) - 1 and self.dfs(board, i, j+1, word[1:]):
                return True

            board[i][j] = word[0] # update the cell to its original value
            return False
        else:
            return False


import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print 'ok'

