#!/usr/bin/env python
# -*- coding: utf8 -*-

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        abs_x = x if x >= 0 else -x
        str_x = str(abs_x)[::-1]
        reverse_x = int(str_x) if x >= 0 else -int(str_x)
        if abs(reverse_x) > 2147483648:
            return 0
        return reverse_x

# 总结：
# 1. 已 0 为结尾的数
# 2. 反转后溢出，返回 0

if __name__ == '__main__':
    print 'ok'
    print Solution().reverse(123)
    print Solution().reverse(-123)
    print Solution().reverse(-324)
    print Solution().reverse(-333)
    print Solution().reverse(111)
    print Solution().reverse(997)
    print Solution().reverse(1534236469)



