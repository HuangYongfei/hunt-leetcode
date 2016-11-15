#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import


# 71. Simplify Path
# Given an absolute path for a file (Unix-style), simplify it.

# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"

# Corner Cases:
# 1. Did you consider the case where path = "/../"?
#    In this case, you should return "/".
# 2. Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
#    In this case, you should ignore redundant slashes and return "/home/foo".

# 总结：
#

class Solution(object):

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        paths = path.split('/')
        res = []
        for x in paths:
            if x == '.' or x == '':
                pass
            elif x == '..':
                if len(res):
                    res.pop()
            else:
                res.append(x)

        return '/' + '/'.join(res) if res else '/'

import unittest


class TestSolution(unittest.TestCase):

    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print(Solution().simplifyPath('/..'))
    print(Solution().simplifyPath('/...'))
    print('ok')
