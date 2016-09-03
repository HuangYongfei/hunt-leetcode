#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 总结：
# 1. 比较当前元素[j]是否和前一个[j-1]的值相同
# 2. 相同, 则计数count +1
# 3. 不同，字符串增加 ： count 个 res[j-1]，同时重新初始count
# 4. 循环结束，字符串需要加上最后 count 个 res[j]
# 5. 得到的新字符串作为下一循环的输入字符串

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'

        res = '11'

        for i in range(2, n):
            count = 1
            temp = ''
            for j in range(1, len(res)):
                if res[j-1] == res[j]:
                    count += 1
                else:
                    temp += str(count) + str(res[j-1])
                    count = 1
            temp += str(count) + str(res[j])
            res = temp
        return res

import unittest
class TestSolution(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1, 1)
        self.assertTrue(True)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    print Solution().countAndSay(1)
    print Solution().countAndSay(2)
    print Solution().countAndSay(3)
    print Solution().countAndSay(4)
    print Solution().countAndSay(5)
    print 'ok'

