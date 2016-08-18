#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 总结:
# 1. 前缀符号：+, -
# 2. 开始部分字符合法，中间有不合法字符
# 3. 正溢出和负溢出
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        num = 0
        s = str.strip()
        if s[0] == '+' or s[0] == '-':
            for x in s[1:]:
                if ord(x) >= 48 and ord(x) <= 57:
                    num = num * 10 + (ord(x) - 48)
                else:
                    break
            if s[0] == '+':
                if num > 2147483647:
                    num = 2147483647
            else:
                if num > 2147483648:
                    num = 2147483648
                num = -num
            return num

        for x in s:
            if ord(x) >= 48 and ord(x) <= 57:
                num = num * 10 + (ord(x) - 48)
            else:
                break
        if num > 2147483647:
            num = 2147483647
        if num < -2147483647:
            num = -2147483647
        return num


if __name__ == '__main__':
    print 'ok'
    print Solution().myAtoi('')
    print Solution().myAtoi('-123')
    print Solution().myAtoi('+123')
    print Solution().myAtoi('123')
    print Solution().myAtoi('a23')
    print Solution().myAtoi('023')
    print Solution().myAtoi('+023')
    print Solution().myAtoi('+-12')
    print Solution().myAtoi('+123a012')
    print Solution().myAtoi('2147483647')
    print Solution().myAtoi('2147483648')
    print Solution().myAtoi('-2147483648')
    print Solution().myAtoi('-2147483649')
    print Solution().myAtoi('1a')

